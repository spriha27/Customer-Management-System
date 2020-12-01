from website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(userid):
    return Existing_user.query.get(int(userid))

class Existing_user(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def get_id(self):
        return self.userid

class Deleted_user(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    contactno = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

class Manager(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def get_id(self):
        return self.userid
