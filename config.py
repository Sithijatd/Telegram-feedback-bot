import os
from os import environ
from os import getenv

class Config(object):
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	SESSION_STRING = environ.get("SESSION_STRING", None)
	OWNER = list(map(int, getenv("OWNER").split())) # ain karanna epa hehe
	MONGODB_URI = os.environ.get("MONGODB_URI")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY"))
	ARQ_API_KEY = os.environ.get("ARQ_API_KEY")

        #Error ekk
       #API_KEY = os.environ.get("HEROKU_API_KEY", None)
       #APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
       #if not API_KEY or \
          #not APP_NAME:
          #HEROKU_APP=None
       #else:
          #HEROKU_APP=heroku3.from_key(API_KEY).apps()[APP_NAME] """

     
