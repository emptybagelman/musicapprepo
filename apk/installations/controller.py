from .model import Installation
from werkzeug import exceptions
from flask import jsonify, request
from apk import db

def index():
    try:
        installations = Installation.query.all()
        data = [inst.json for inst in installations]
        return jsonify({"installations":data})
    except:
        raise exceptions.InternalServerError("Oh no")
    
def create():
    try:
        print("❌❌❌", request)
        # print("🌕🌕🌕🌕", request.get_json())

        name = request.form.get("name")
        version = request.form.get("version")
        directory = request.form.get("directory")
        resolution = request.form.get("resolution")
        javaexec = request.form.get("javaexec")
        jvm = request.form.get("jvm")
        new_inst = Installation(name=name,version=version,directory=directory,resolution=resolution,javaexec=javaexec,jvm=jvm)

        db.session.add(new_inst)
        db.session.commit()

        return jsonify({"new_installation":new_inst.json}),201
    except:
        raise exceptions.BadRequest("CRACK")