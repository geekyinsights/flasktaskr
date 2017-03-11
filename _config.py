import os

#grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'U496Kz2jY7yLvw5Jb06M6S7eW76aD4GW'

#define the full path for DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
