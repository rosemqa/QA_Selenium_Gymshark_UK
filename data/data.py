import os
from dotenv import load_dotenv

load_dotenv()


class AutData:
    USER_FIRST_NAME = 'Ccc'
    LOGIN_EMAIL = 'sekamay355@kazvi.com'
    PASSWORD = os.getenv('PASSWORD')
