import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
bootstrap = Bootstrap(app)

from app import views, models
