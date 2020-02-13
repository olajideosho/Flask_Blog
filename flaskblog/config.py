import os

class Config:
    SECRET_KEY = 'cb3eb3d56e9f2dec80faba2ac9f9d669'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'aaaa@aaaa.com'
    MAIL_PASSWORD = 'aaaa@aaaa.com'