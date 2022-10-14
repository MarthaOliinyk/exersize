from os import getenv
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

db = SQLAlchemy(app)

jwt = JWTManager(app)

import src.resourse
from src.model.revoked_tokens import RevokedTokens


@app.before_request
def create_tables():
    db.create_all()


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(header, decrypted_token):
    jti = decrypted_token['jti']

    return RevokedTokens.is_jti_blacklisted(jti)
