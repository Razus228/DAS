from datetime import datetime
from modules.database import db

class message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self, sender, message):
        self.sender = sender
        self.message = message
        self.date = datetime.utcnow()

