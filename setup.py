import setuptools

from textwrap import dedent

setuptools.setup(
    name='trello',
    version='0.9.7.3',
    packages=['trello'],
    license='3-Clause BSD License (https://opensource.org/licenses/BSD-3-Clause)',
    description='Python library for interacting with the Trello API',
    long_description_content_type='text/markdown',
    long_description="""Python Trello API Wrapper
=========================

This library is a Python wrapper around the [Trello](https://trello.com/) REST API.

Requires Python 3.6 or later.

If you wish to use this with Python 2 or Python 3.5 or lower, please use version 0.9.4.

Getting Started
---------------

To use the Python API, first install it from PyPI using `pip`:

    pip install trello

or from source:

    python setup.py install

Once you have it installed, get an API key from [https://trello.com/app-key](https://trello.com/app-key).

    >>> from trello import TrelloApi
    >>> trello = TrelloApi(TRELLO_APP_KEY)
    >>> trello.boards.get('4d5ea62fd76aa1136000000c')
    {
        "closed": false, 
        "desc": "Trello board used by the Trello team to track work on Trello.  How meta!", 
        "id": "4d5ea62fd76aa1136000000c", 
        "idOrganization": "4e1452614e4b8698470000e0", 
        "name": "Trello Development", 
        "pinned": true, 
        "prefs": {
            "comments": "public", 
            "invitations": "members", 
            "permissionLevel": "public", 
            "voting": "public"
        }, 
        "url": "https://trello.com/board/trello-development/4d5ea62fd76aa1136000000c"
    }

Because the Trello development board is public, we didn't need a user's token, but if we want to access private boards, we'll have to have one. We can get it by calling:

    >>> trello.get_token_url('My App', expires='30days', write_access=True)
        'https://trello.com/1/authorize?key=TRELLO_APP_KEY&name=My+App&expiration=30days&response_type=token&scope=read,write'

If you send your user to the resulting URL, it will ask them to allow your app access to their account, and then it will give them a token (64-digit hex string) that they will pass back to your app.

    >>> trello.set_token(user_token)

(*Note: Trello does support OAuth, but the Python API does not have any support for it yet.*)

Once you have set the user's token, all calls to the API will include that token, as if the user was logged in.""",
    author='tghw,kulikjak,waghanza,lukegb,lazytarget',
    author_email='ty@tghw.com',
    url='https://github.com/tghw/trello-py',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    install_requires = [
        "requests",
    ],
    python_requires='>=3.6',
)
