from datetime import datetime
from app import db 

#blog table

class Blog(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(120), index=True)
    sub_title=db.Column(db.String(120))
    image=db.Column(db.String )
    date_posted=db.Column(db.DateTime, default=datetime.now)
    content=db.Column(db.Text)

    def __repr__(self):
        
        return f"User('{self.title}','{self.sub_title}','{self.date_posted}')"