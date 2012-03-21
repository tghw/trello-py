import os
import re
import requests
import pystache
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup as Soup

INDEX = 'https://trello.com/docs/api/index.html'

METHOD_LOOKUP = {
    'GET': 'get',
    'PUT': 'update',
    'POST': 'new',
    'DELETE': 'delete',
}

def get_soup(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return Soup(resp.content)

def main():
    sections = get_sections()
    print sections
    if not os.path.exists('trello'):
        os.mkdir('trello')
    modules = []
    for section in sections:
        write_section(section)

    with open(os.path.join('trello', '__init__.py'), 'w') as fd:
        trello_api = TrelloApi([module_name(section) for section in sections])
        fd.write(trello_api.render())

def get_sections():
    sections = []
    soup = get_soup(INDEX)
    for li in soup.findAll('li', {'class': 'toctree-l1'}):
        a = li.find('a', {'class': 'reference internal'})
        sections.append(urljoin(INDEX, a['href']))
    return sections

def get_actions(section_url):
    actions = []
    soup = get_soup(section_url)
    for section in soup.find('div', {'class': 'section'}).findAll('div', {'class': 'section'}):
        h2 = section.find('h2')
        method, url, _ = [s.strip() for s in h2.findAll(text=True)]
        ul = section.ul
        args = []
        for li in ul.findAll('li', recursive=False):
            if 'arguments' in li.text.lower():
                args_ul = li.ul
                if args_ul:
                    for arg_li in args_ul.findAll('li', recursive=False):
                        arg = arg_li.tt.text
                        required = 'required' in arg_li.text.lower()
                        args.append((arg, required))
        actions.append((method, url, args))
    return actions

def function_args(url_args, id_arg, req_args, opt_args):
    if id_arg:
        req_args = [id_arg] + req_args
    return ', '.join(url_args + req_args + [arg + '=None' for arg in opt_args])

def request_args(request_type, req_args, opt_args):
    get_args = []
    post_args = []
    if request_type in ['GET', 'DELETE']:
        get_args += req_args
        get_args += opt_args
    else:
        post_args += req_args
        post_args += opt_args
    params = 'dict(%s)' % ', '.join(['key=self._apikey', 'token=self._token'] + ['%s=%s' % (arg, arg) for arg in get_args])
    data = 'dict(%s)' % ', '.join(['%s=%s' % (arg, arg) for arg in post_args]) if post_args else None
    return 'params=%s, data=%s' % (params, data)

def module_name(section_url):
    return section_url.split('/')[-2] + 's'

def write_section(section_url):
    module = module_name(section_url)
    with open(os.path.join('trello', '%s.py' % module), 'w') as fd:
        fd.write(ApiClass(section_url).render())

class ApiClass(pystache.View):
    def __init__(self, section_url):
        super(ApiClass, self).__init__()
        self.module = module_name(section_url)
        self.actions = get_actions(section_url)

    def class_name(self):
        return self.module.title()

    def methods(self):
        methods = []
        for action in self.actions:
            url_parts = action[1].split('/')
            method_parts = [part.rstrip('s') for part in url_parts[3:] if not part.startswith('[')]
            method_name = '_'.join([METHOD_LOOKUP[action[0]]] + method_parts)
            id_arg = ([part.strip('[]').replace(' ', '_') for part in url_parts if part.startswith('[')] or [None])[0]
            url_args = [arg[0] for arg in action[2] if ('[%s]' % arg[0] in url_parts)]
            if url_args:
                method_name  = '%s_%s' % (method_name, '_'.join(url_args))
            req_args = [arg[0] for arg in action[2] if arg[1] and arg[0] not in url_args]
            opt_args = [arg[0] for arg in action[2] if not arg[1]]
            def_args = function_args(url_args, id_arg, req_args, opt_args)
            args = request_args(action[0].upper(), req_args, opt_args)
            method = action[0].lower()
            url = '"https://trello.com%s" %% (%s)' % (re.sub(r'\[.*?\]', '%s', action[1]), ', '.join([id_arg] + url_args if id_arg else url_args))
            methods.append(dict(def_args=def_args, args=args, method=method, url=url, name=method_name))
        return methods

class TrelloApi(pystache.View):
    def __init__(self, sections):
        super(TrelloApi, self).__init__()
        self.sections = [{'module': section, 'class': section.title()} for section in sections]

if __name__ == '__main__':
    main()
