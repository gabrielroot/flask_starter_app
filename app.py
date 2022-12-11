from decouple import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI', default='sqlite:///data.db')
app.config['SQLALCHEMY_ECHO'] = config('SQLALCHEMY_ECHO')

db = SQLAlchemy(app)

migrate = Migrate(app, db)
from models import *

@app.route("/")
def hello_world():
    return render_template('index.html')

from routes.user import user_routes
app.register_blueprint(user_routes)