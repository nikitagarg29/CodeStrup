from flask import Flask
import app.config

app = Flask(__name__)
app.config['SECRET_KEY'] = "no"
from app import routes