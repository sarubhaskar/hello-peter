import db

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Peter!'

@app.route("/quotes.json")
def index():
    return db.quotes_all()