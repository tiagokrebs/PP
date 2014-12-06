from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
# Blueprints
from main import main as main_blueprint

# Cria instancias dos apps
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

# Cria Facoty e inicializa apps e modulos blueprints
def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)
  
  bootstrap.init_app(app)
  mail.init_app(app)
  moment.init_app(app)
  db.init_app(app)
  
  # Registro Blueprints
  #app.register_blueprint(main_blueprint, url_prefix='/another_prefix_to_main')
  app.register_blueprint(main_blueprint)
  
  return app