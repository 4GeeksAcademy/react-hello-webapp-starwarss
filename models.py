from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    favorites = db.relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    height = db.Column(db.String(50))
    mass = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))

    def __repr__(self):
        return f'<People {self.name}>'

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    population = db.Column(db.String(50))

    def __repr__(self):
        return f'<Planet {self.name}>'
    
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    model = db.Column(db.String(80), nullable=False)
    manufacturer = db.Column(db.String(80), nullable=False)
    passengers = db.Column(db.String(20))
    crew = db.Column(db.String(20))
    length = db.Column(db.String(20))
    max_atmosphering_speed = db.Column(db.String(20))

    def __repr__(self):
        return f'<Vehicle {self.name}>'


class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=True)  # Corrigido vehicles_id para vehicle_id

    def __repr__(self):
        return f'<Favorite User: {self.user_id} Planet: {self.planet_id} People: {self.people_id} Vehicle: {self.vehicle_id}>'

