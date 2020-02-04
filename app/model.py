from app import db


#creating an database model
class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)
    name_=db.Column(db.String(120))

    def __init__(self, email_, height_,name_):
        self.email_=email_
        self.height_=height_
        self.name_=name_
