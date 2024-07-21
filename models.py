from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_type = db.Column(db.String(10), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    files = db.relationship('File', backref='user', lazy=True)

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "user_type": self.user_type,
            "verified": self.verified
        }

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

