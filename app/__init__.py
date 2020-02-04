
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser



app = Flask(__name__)



cfg = ConfigParser()
cfg.read_file(open('configure/cfg.ini'))
email_id=cfg.get('email','email_id')
password=cfg.get('email','password')
URI= cfg.get('database', 'database_uri')



#connecting to my local mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = URI




#creating an SQLAlchemy object
db = SQLAlchemy(app)
app.secret_key = cfg.get('settings', 'secret_key')


from app import routes