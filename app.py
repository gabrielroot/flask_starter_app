from decouple import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI', default='sqlite:///data.db')
app.config['SQLALCHEMY_ECHO'] = config('SQLALCHEMY_ECHO')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)



@app.route("/")
@app.route("/<var>")
def hello_world(var=''):
    with app.app_context():
      print('here xxxxx')
      db.create_all()
      print('here vvvvv')
    return render_template('index.html', name=var)