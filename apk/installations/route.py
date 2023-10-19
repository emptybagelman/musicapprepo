from flask import jsonify, request
from werkzeug import exceptions
from apk import app, db
from apk.installations.model import Installation
from apk.installations.controller import index, create

@app.route("/installations",methods=["GET","POST"])
def handle_installations():
    if request.method == "GET":
        return index()
    if request.method == "POST":
        return create()
    

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error":f"Server is fucked {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error":f"We fucked it {err}"}), 500

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error":f"That's a shit request {err}"}), 400