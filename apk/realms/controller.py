from .model import Realm
from werkzeug import exceptions
from flask import jsonify, request
from apk import db

def index():
    try:
        realms = Realm.query.all()
        data = [realm.json for realm in realms]
        return jsonify({"realms":data})
    except:
        raise exceptions.InternalServerError("Oh no")