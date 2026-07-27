import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-desenvolvimento'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///finance.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False