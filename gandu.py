
from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_KEY = config("API_KEY", default=6, cast=int)
    API_HASH = config("API_HASH", None)
    TOKEN = config("TOKEN", None)
    OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
