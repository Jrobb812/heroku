import os
from flask import Flask, json, jsonify, request
from requests.models import HTTPBasicAuth 
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random_string'
auth = HTTPBasicAuth(username, password)

class ValidationError(ValueError):
    pass

users = {
    "vcu": generate_password_hash("rams")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
        check_password_hash(users.get(username), password):
        return username

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'Page not found.'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Something broke'}), 500

@app.route('/ping', methods = ['GET'])
@auth.login_required
def index():
    return "Time taken: "
