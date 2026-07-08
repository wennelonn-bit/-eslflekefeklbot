from os import environ 

class Config:
    API_ID = environ.get("API_ID", "35018640")
    API_HASH = environ.get("API_HASH", "44dc330c7d9c2363e3f6abcd223a7334")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8920587998:AAGQebFs3qUKXqSE9vH5ZfSKs6ehCrWSe0o") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://bot_user:frwgSseHgO1bZrpO@cluster0.mwdg6aw.mongodb.net/?appName=Cluster0&tlsAllowInvalidCertificates=true")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8625210354').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
