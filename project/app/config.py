from flask import Flask
from flask_codemirror import CodeMirror
import os


# mandatory
CODEMIRROR_LANGUAGES = ['python', 'html']
WTF_CSRF_ENABLED = False
SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
# optional
CODEMIRROR_THEME = '3024-day'
CODEMIRROR_ADDONS = (
        ('ADDON_DIR','ADDON_NAME'),
)

app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)