from os import environ 

class Config:
    API_ID = environ.get("API_ID", "35018640")
    API_HASH = environ.get("API_HASH", "44dc330c7d9c2363e3f6abcd223a7334")
    BOT_TOKEN = environ.get("BOT_TOKEN", "9168361449:AAFF_N2hnR616r8MROsyFPpdW3oR31k8mDI") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://bot_user:YgUSLmGBgPyCFzuf@cluster0.mwdg6aw.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8625210354').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
