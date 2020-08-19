from os import environ, path
from dotenv import load_dotenv

rootdir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(rootdir, '.env'))

TESTING = True
DEBUG = True
FLASK_ENV = 'development'