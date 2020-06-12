from datetime import datetime
from application import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    # 0 for not 1 yes
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repe__(self):
        return '<Task %r>' % self.id

