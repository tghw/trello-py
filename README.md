Python Trello API Wrapper
=========================

This Python API is simply a wrapper around the [Trello](https://trello.com/) REST API.

This library requires Python 3.6 or later. If you wish to use this with Python 2 or Python 3.5 or lower, please use version 0.9.4.

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
        "desc": "Trello board used by the Trello team to track work on Trello.  How meta!\n\nThe development of the Trello API is being tracked at https://trello.com/api\n\nThe development of Trello Mobile applications is being tracked at https://trello.com/mobile", 
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

Once you have set the user's token, all calls to the API will include that token, as if the user was logged in.