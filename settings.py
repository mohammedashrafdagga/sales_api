from dotenv import load_dotenv
import os

# load evn variable
load_dotenv()

# get access to env variable 
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_server = os.environ.get('DB_SERVER')
db_name = os.environ.get('DB_NAME')

#  Global Variable
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_server}/{db_name}"
