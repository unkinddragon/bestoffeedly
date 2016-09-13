from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):
    __abstract__  = True
    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):
    __tablename__ = 'users'

    name     = db.Column(db.String(128),  nullable=False, unique=True)
    email    = db.Column(db.String(128),  nullable=True)
    password = db.Column(db.String(192),  nullable=False)
    status   = db.Column(db.String(32), nullable=False)

    def __init__(self, name, password):

        self.name     = name
        self.email    = email
        self.password = password
        self.status   = 'active'

        # get all permissions for the user

    def __repr__(self):
        return '<User %r>' % (self.name)

class Permission(Base):
    __tablename__ = 'permissions'

    name    = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    value   = db.Column(db.Boolean, default=False)

    def __init__(self, name, user_id, value=False):
        self.name   = name
        self.user_id= user_id
        self.value  = value