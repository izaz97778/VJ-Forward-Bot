# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ

class Config:
    try:
        API_ID = int(environ["API_ID"])
        BOT_OWNER = int(environ["BOT_OWNER"])
    except KeyError as e:
        raise ValueError(f"Missing required environment variable: {e.args[0]}")
    except ValueError as e:
        raise ValueError("API_ID and BOT_OWNER must be integers.")

    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "")
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot")
    DATABASE_URI = environ.get("DATABASE_URI", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
