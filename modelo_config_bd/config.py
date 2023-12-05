from flask import *
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
from datetime import timedelta
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='C:/Users/Lucas Andrei/ficha-rpg-online/templates',
static_folder='C:/Users/Lucas Andrei/ficha-rpg-online/templates/static')
CORS(app)  

path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'rpg.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)