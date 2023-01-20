# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 23098568))
    API_HASH = os.environ.get("API_HASH", "cb7098aa919c29da3e5f9af0f9086dd7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5850952542:AAEF-Y3P7gIy2K1zbYyqfmnqgTQxNpt978s")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "Mdisk Search Bot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOL4Bu8UNyJ-TIOIvyDAJi4lzcDBjMmvc_xYC2MgZSYR1kNl2eFtrp4hgvAW4u0-RuDe4QbNMZDAX48EwZN__qqeTUBPeFAvN8XLcFvqBOJhzvNjezgsQm85BiKpW8dlOtruTLwLG_Hsctx21ZdjuCapMYyRJMx7dgms7VA2Da9Bm30M6gAliuZas1V2s09JybCci6Ml3qsv3wS4Up38zv8mEEuk1t_AbSy51KH4hBQKSZwi9JqbGsHeHa5crNKy8Ua7Aw1cluNAw3fICTQySkKctdd5fC9YzDOo84xuml1t0uRtm58GsBn1-yIJxuOMf6N9rnn9gcwiivHIVjXXqrrnMtYs=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001575849076))
    BOT_USERNAME = os.environ.get("mdisk_movies_searchbot")
    BOT_OWNER = int(os.environ.get("5183104181"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001738397533)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/Mdisk_Links_Sender_Bot>Mdisk_Links_Sender_Bot</a>

📝 Language: <a href='https://www.python.org'> Python V3 </a>

📚 Library: <a href='https://docs.pyrogram.org'> Pirogram </a>

📡 Server: <a href='https://heroku.com'> Heroku/Github </a>

👨‍💻 Developed By: <a href='https://t.me/Z_Harbour_bot'> Z_Harbour_bot </a> </b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer: Anonymous </b>

<u> Source Code Is Private For Privacy</b> </u>
"""

    HOME_TEXT = """

<b>Hello Dear {} 😘

<a>I'm Mdisk Search Robo</a>

I Can Search Any Stuff!🔍 What do You Want?Just Drop A Name!☺️

"""


    START_MSG = """
<b>Hello Dear {} 😘

<a>I'm Mdisk Search Robo</a></b>

<i> I Can Search Any Mobi-Seriez-Showz! And Can Provide You Direct Mdisk Links! If Found On My Database:) </i>

<a> If You Didn't Find Your Query Then Please Request on @blackest_harbour❤😊 </a>
"""


