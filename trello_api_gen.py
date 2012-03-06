import os
import re
import requests
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
    for section in sections:
        write_section(section)

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

def def_args(req_args, opt_args):
    return ', '.join(req_args + [arg + '=None' for arg in opt_args])

def write_section(section_url):
    module = section_url.split('/')[-2]
    if not os.path.exists('trello'):
        os.mkdir('trello')
    actions = get_actions(section_url)
    with open(os.path.join('trello', '%s.py' % module), 'w') as fd:
        for action in actions:
            url_parts = action[1].split('/')
            method_parts = [part.rstrip('s') for part in url_parts[2:] if not part.startswith('[')]
            method_name = '%s_%s' % (METHOD_LOOKUP[action[0]], '_'.join(method_parts))
            id_arg = [part.strip('[]').replace(' ', '_') for part in url_parts if part.startswith('[')]
            id_arg = id_arg[0] if id_arg else None
            req_args = [arg[0] for arg in action[2] if arg[1]]
            opt_args = [arg[0] for arg in action[2] if not arg[1]]
            args = req_args + opt_args
            if id_arg:
                print >>fd, 'def %s(%s, %s):' % (method_name, id_arg, def_args(req_args, opt_args))
                print >>fd, '    resp = requests.%s("%s" %% %s, %s)' % (action[0].lower(), re.sub(r'\[.*\]', '%s', action[1]), id_arg, ', '.join(args[1:]))
            else:
                print >>fd, 'def %s(%s):' % (method_name, def_args(req_args, opt_args))
                print >>fd, '    resp = requests.%s("%s", %s)' % (action[0].lower(), action[1], ', '.join(args))
            print >>fd, '    resp.raise_for_status()'
            print >>fd, '    return json.loads(resp.content)'
            print >>fd, ''

if __name__ == '__main__':
    main()
