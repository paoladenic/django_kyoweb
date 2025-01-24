import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# mysqlclient
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('SQL_NAME'),
        'USER': os.getenv('SQL_USER'),
        'PASSWORD': os.getenv('SQL_PASSWORD'),
        'HOST': os.getenv('SQL_HOST'),
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
