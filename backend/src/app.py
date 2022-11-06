from os import getenv
from flask import Flask
from datetime import timedelta
from dotenv import load_dotenv
from flask_cors import CORS
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

load_dotenv()
app = Flask(__name__)
cors = CORS(app)

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


@app.after_request
def cors_origin(response):
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, " \
                                                       "X-Requested-With "
    return response


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(header, decrypted_token):
    jti = decrypted_token['jti']

    return RevokedTokens.is_jti_blacklisted(jti)
