from .db import db

class UserEntity(db.Document):
    firstName = db.StringField(required=True)
    lastName = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)