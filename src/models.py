from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# pipenv run migrate create database migrations (if models.py is edited), only first 2 are needed
# pipenv run upgrade run database migrations (if pending)
# pipenv run start start flask web server (if not running)
# pipenv run deploy deploy to heroku (if needed)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    # password = db.Column(db.String(80), unique=False, nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)
    label = db.Column(db.String(80), unique=False, nullable=False)
    done = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.label

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "email": self.email,
    #         # do not serialize the password, its a security breach
    #     }
    
    def serialize(self):
        return {
            "label": self.label,
            "done": self.done,
            "username": self.username,
            "id": self.id
            # do not serialize the password, its a security breach
        }