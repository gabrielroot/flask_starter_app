from decouple import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI', default='sqlite:///data.db')
app.config['SQLALCHEMY_ECHO'] = config('SQLALCHEMY_ECHO')

db = SQLAlchemy(app)

migrate = Migrate(app, db)
from models import User

@app.route("/")
@app.route("/<var>")
def hello_world(var=''):
    return render_template('index.html', name=var)
  
# Separar rotas (blueprints), usar wtforms