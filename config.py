from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("")

API_ID = int(os.environ.get("API_ID", ''))
API_HASH = getenv("")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", ""))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
