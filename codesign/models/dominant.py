from codesign import db

class Dominant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50))
    def __init__(self,color):
        self.color = color

