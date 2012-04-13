Examples
========

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
