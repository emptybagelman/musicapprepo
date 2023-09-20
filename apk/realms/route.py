from flask import jsonify, request
from werkzeug import exceptions
from apk import app, db
from apk.realms.model import Realm
from apk.realms.controller import index

@app.route("/realms",methods=["GET"])
def handle_realms():
    if request.method == "GET":
        return index()
    
