import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

def get_keys(path):
    with open(path) as f:
        return json.load(f)

app.config['SECRET_KEY'] = get_keys(".secret/secrets.json")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'feedback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    feedback_description = db.Column(db.Text)

    def __init__(self, name, feedback_description):
        self.name = name
        self.feedback_description = feedback_description