from allpy import db, login_manager
from allpy import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    iq = db.Column(db.Integer(), nullable=False, default=0)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, passwd):
        self.password_hash = bcrypt.generate_password_hash(passwd).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)