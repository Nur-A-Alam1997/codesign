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
