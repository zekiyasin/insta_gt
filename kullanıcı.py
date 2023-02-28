# pull credentials from .env file
import os
from dotenv import load_dotenv
load_dotenv()


userName = os.environ.get("USER")
password = os.environ.get("PASSWORD")
