from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
