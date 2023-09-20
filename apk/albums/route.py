from flask import jsonify, request
from werkzeug import exceptions
from apk import app, db
from apk.albums.model import Album
from apk.albums.controller import index, create, get_by_id, update, destroy


@app.route("/")
def hello_world():
    return jsonify({
        "message":"Welcome",
        "description":"albums API",
        "endpoints":[
            "GET /"
        ]
    }), 200

@app.route("/albums",methods=["GET","POST"])
def handle_albums():
    if request.method == "POST":
        return create()
    if request.method == "GET":
        return index()


@app.route("/albums/<int:id>",methods=["GET","PATCH","DELETE"])
def get_album(id):
    if request.method == "GET":
        return get_by_id(id)
    if request.method == "PATCH":
        return update(id)
    if request.method == "DELETE":
        return destroy(id)
    



@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error":f"Server is fucked {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error":f"We fucked it {err}"}), 500

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error":f"That's a shit request {err}"}), 400