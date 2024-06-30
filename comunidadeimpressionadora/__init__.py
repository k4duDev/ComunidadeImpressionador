from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '28d16c04'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

db = SQLAlchemy(app)

from comunidadeimpressionadora import routes