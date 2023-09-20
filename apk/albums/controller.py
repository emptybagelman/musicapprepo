from .model import Album
from werkzeug import exceptions
from flask import jsonify, request
from apk import db

def index():
    try:
        albums = Album.query.all()
        data = [c.json for c in albums]
        return jsonify({"albums":data})
    
    except:
        raise exceptions.InteralServerError("Ah shit")
    
def create():
    try:
        print("❌❌❌", request)
        # print("🌕🌕🌕🌕", request.json.values())
        name,age,catch_phrase = request.json.values()
        new_artist = Album(name=name,age=age,catch_phrase=catch_phrase)

        db.session.add(new_artist)
        db.session.commit()

        return jsonify({"newchar":new_artist.json}),201
    except:
        raise exceptions.BadRequest("Balls")
    
def get_by_id(id):
    try:
        album = Album.query.filter_by(id=id).first()
        return jsonify({"data":album.json}), 200
    except:
        raise exceptions.NotFound("You know")
    
def update(id):
    try:
        data = request.json
        album = Album.query.filter_by(id=id).first()

        for (attribute,value) in data.items():
            if hasattr(album,attribute):
                setattr(album, attribute, value)

        db.session.commit()

        return jsonify({"data":album.json})
    except:
        pass

def destroy(id):
    try:
        album = Album.query.filter_by(id=id).first()
        db.session.delete(album)
        db.session.commit()
        return f"album {album.name} deleted."
    except:
        pass