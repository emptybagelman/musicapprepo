from apk import db, app

app.app_context().push()

class Installation(db.Model):
    __tablename__ = "installations"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    version = db.Column(db.String(100),nullable=False)
    directory = db.Column(db.String(100),nullable=False)
    resolution = db.Column(db.String(100), nullable=False)
    javaexec = db.Column(db.String(200),nullable=True)
    jvm = db.Column(db.String(200),nullable=True)

    def __repr__(self):
        return f"Installation(id: {self.id}, name: {self.name}, version: {self.version}, directory: {self.directory}, resolution: {self.resolution}, javaexec: {self.javaexec}, jvm: {self.jvm})"
    
    @property
    def json(self):
        return {"id": self.id, "name": self.name, "version": self.version, "directory": self.directory, "resolution": self.resolution, "javaexec": self.javaexec, "jvm": self.jvm}