from os import environ 

class Config:
    API_ID = environ.get("API_ID", "35018640")
    API_HASH = environ.get("API_HASH", "d44dc330c7d9c2363e3f6abcd223a7334")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8920587998:AAHMkBEvgZIkcWMejiJ28sW_mFaQsIlI3v4") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
