from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment-01.db'
app.config['SECRET_KEY'] = 'd38f517fdac19aa6ba4052ef6173d8c2bd1fda52ed94ffea6a585516ff40dd7a';
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_page'

from project import routes