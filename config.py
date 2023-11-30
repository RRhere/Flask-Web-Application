# config.py
import os
import smtplib, ssl

SECRET_KEY = '12345'
SQLALCHEMY_DATABASE_URI = 'sqlite:///temp1.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Mail configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'onlyhomeworkify@gmail.com'
MAIL_PASSWORD = 'koyaxxgznrhnvayc'
MAIL_DEFAULT_SENDER = 'onlyhomeworkify@gmail.com'
