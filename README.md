Python Trello API Wrapper
=========================

This library is a Python wrapper around the [Trello](https://trello.com/) REST API.

Requires Python 3.8 or later.

Getting Started
---------------

Once you have it installed, get an API key from [https://trello.com/app-key](https://trello.com/app-key).


To Acquire the specific token to run the Trello Wrapper, one must submit for and store a unique OAUTH Token.

    >>> trello_api = trello.TrelloAPI(apikey) -> where apikey is the supplied API Key from Trello
    >>> trello.get_token_url('My App', expires='30days', write_access=True)
        'https://trello.com/1/authorize?key=TRELLO_APP_KEY&name=My+App&expiration=30days&response_type=token&scope=read,write'
        " expired choices ['1day', '10day'. '30day', 'none']

If you send your user to the resulting URL, it will ask them to allow your app access to their account, and then it will give them a token (64-digit hex string) that they will pass back to your app.

    >>> trello.set_token(user_token)

Once you have set the user's token, all calls to the API will include that token, as if the user was logged in.


Trello REST API Documentation
=============================
This is the address to where all the currently written 'classes' work around. `https://developer.atlassian.com/cloud/trello/rest/api-group-actions/#api-group-actions`

Documentation and Guide to Atlassian API `https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/`



