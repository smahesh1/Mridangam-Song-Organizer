from app import db


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    ragam = db.Column(db.String(64), index=True)
    talam = db.Column(db.String(64), index=True)
    artist = db.Column(db.String(64), index=True)
    link = db.Column(db.String(255))

    def __repr__(self):
        return '<Song %r>' % (self.name)

