from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


DEFAULT_PHOTO = 'https://expertphotography.com/wp-content/uploads/2019/02/pet-photography-image.jpg'


class Pet(db.Model):
    """Pet schema.

    Includes id as a primary key, name, spceies, photo_url with a default
    value, age, notes, and an availability boolean. 
    """

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default=DEFAULT_PHOTO)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)


def connect_db(app):
    db.app = app
    db.init_app(app)
