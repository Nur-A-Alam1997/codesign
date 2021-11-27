from codesign import db
class Favourite(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50))
    fav = db.Column(db.String(80))
    def __init__(self,owner, fav):
        self.owner = owner
        self.fav = fav
