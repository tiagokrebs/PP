import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuracao geral
class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'd9b773cd3f4dccf50a372ccfd34199b3'
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  PP_MAIL_SUBJECT_PREFIX = '[PP]'
  PP_MAIL_SENDER = 'PP Admin <admin@pp.com.br>'
  PP_ADMIN = os.environ.get('PP_ADMIN')

  @staticmethod
  def init_app(app):
    pass

# Cinfiguracao de ambientes
class DevelopmentConfig(Config):
  DEBUG = True
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.enviton.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    
class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
  'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
  'production': ProductionConfig,

  'default': DevelopmentConfig
}