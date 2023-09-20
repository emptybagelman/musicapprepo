from apk import db, app

app.app_context().push()

class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer,primary_key=True)
    album_name = db.Column(db.String(100),nullable=False)
    songs = db.Column(db.String,nullable=False)

    def __repr__(self):
        return f"Album(id: {self.id}, album_name: {self.album_name}, songs: {self.songs})"
    
    @property
    def json(self):
        return {"id": self.id, "album_name": self.album_name, "songs": self.songs}