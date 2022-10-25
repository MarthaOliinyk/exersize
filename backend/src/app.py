from os import getenv
from flask import Flask
from datetime import timedelta
from dotenv import load_dotenv
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

app.config["WTF_CSRF_ENABLED"] = False
app.config["JWT_COOKIE_CSRF_PROTECT"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

db = SQLAlchemy(app)

jwt = JWTManager(app)

import src.resourse
from src.model.revoked_tokens import RevokedTokens


@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    user_agent = reqparse.request.headers.get('User-Agent')
    ip = reqparse.request.environ['REMOTE_ADDR']

    return {
        'user_agent': user_agent,
        'ip': ip
    }


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(header, decrypted_token):
    jti = decrypted_token['jti']

    return RevokedTokens.is_jti_blacklisted(jti)
