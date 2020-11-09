import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_sqlalchemy import SQLAlchemy
import pymysql

class Config:
    SECRET_KEY = 'hard to guess string'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '384971024@qq.com'
    MAIL_PASSWORD = 'ewuwlsvrmihocaja'
    FLASKY_MAIL_SUBJECT_PREFIX = '[议会]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <384971024@qq.com>'
    FLASKY_ADMIN = '384971024@qq.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod  
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:980518@localhost/online_test'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
