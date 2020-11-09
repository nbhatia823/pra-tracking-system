from flask import Flask, render_template, request, redirect, flash, Blueprint
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

from classes.pra import Pra
from db import Db
from api import pra_api

app = Flask(__name__)
CORS(app, resources={
     r"/api/*": {"origins": ["http://localhost:8080", "https://mdh-pra-tracking.netlify.app"]}})


app.register_blueprint(pra_api)

app.secret_key = 'the random string'

csrf = CSRFProtect(app)
app.config['WTF_CSRF_ENABLED'] = False

if __name__ == "__main__":
    app.run(debug=True)
