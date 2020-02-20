import os

BOT_NAME = os.environ.get("BOT_NAME", "")
CSE_KEY = os.environ.get("CSE_KEY", "AIzaSyAK_DuBPeT3FqmM5bJBPNr4GsXn_bzPPI4")
CSE_CX = os.environ.get("CSE_CX", "004252895839609360346:qebiwynb6je")
API_TOKEN = os.environ.get("API_TOKEN", "1077231471:AAHyLN7R92fhrs130cKTN8t6H_1RuG-qkdE")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "https://git.heroku.com/succpic.git")
NGINX_SUBPATH = os.environ.get("NGINX_SUBPATH", "")
BATCH = int(os.environ.get("BATCH", 10))
POLLING = bool(os.environ.get("POLLING", False))
