import db
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, Peter!'

@app.route("/quotes.json")
def index():
    return db.quotes_all()

@app.route("/quotes.json", methods=["POST"])
def create():
    body = request.form.get("body")
    rarity = request.form.get("rarity")
    return db.quotes_create(body, rarity)

@app.route("/quotes/<id>.json", methods=["PATCH"])
def update(id):
    body = request.form.get("body")
    rarity = request.form.get("rarity")
    return db.quotes_update_by_id(id, body, rarity)

@app.route("/quotes/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.quotes_destroy_by_id(id)