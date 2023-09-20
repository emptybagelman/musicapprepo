from apk import db, app

app.app_context().push()

class Realm(db.Model):
    __tablename__ = "realms"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    expired = db.Column(db.Boolean,nullable=False)
    members = db.Column(db.Integer,nullable=True)

    def __repr__(self):
        return f"Realm(id: {self.id}, name: {self.name}, expired: {self.expired}, members: {self.members})"
    
    @property
    def json(self):
        return {"id": self.id, "name": self.name, "expired": self.expired, "members": self.members}