from codesign import db
from codesign.models.dominant import Dominant
from codesign.models.accent import Accent


dominant = [
    Dominant("red"),
    Dominant("blue"),
    Dominant("green"),
    Dominant("yellow"),
    Dominant("purple"),
    Dominant("indigo"),
    Dominant("orange")
    ]

accent = [
    Accent("red"),
    Accent("blue"),
    Accent("green"),
    Accent("yellow"),
    Accent("purple"),
    Accent("indigo"),
    Accent("orange")
    ]

if __name__ == '__main__':
    db.create_all()
    db.session.add_all(dominant)
    db.session.add_all(accent)
    db.session.commit()