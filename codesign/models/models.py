from codesign import db

class Pallete(db.Model):  

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50))
    name = db.Column(db.String(50))
    dominant = db.Column(db.String(50))
    accent = db.Column(db.String(50))
    state = db.Column(db.Boolean)
    def __init__(self,owner, name, dominant, accent, state):
        self.owner = owner
        self.name = name
        self.dominant = dominant
        self.accent = accent
        self.state = state

class Favourite(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50))
    fav = db.Column(db.String(80))
    def __init__(self,owner, fav):
        self.owner = owner
        self.fav = fav

class Dominant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50))
    def __init__(self,color):
        self.color = color

class Accent(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50))
    def __init__(self,color):
        self.color = color
