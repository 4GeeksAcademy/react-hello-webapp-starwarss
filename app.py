from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, People, Planet, User, Favorite, Vehicle

app = Flask(__name__)

# Configurações de banco de dados (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar banco de dados e migrações
db.init_app(app)
migrate = Migrate(app, db)

# Rota principal
@app.route('/')
def index():
    return jsonify({"message": "Bem-vindo à Star Wars REST API!"})

# Endpoint para listar todas as rotas disponíveis
@app.route('/routes', methods=['GET'])
def get_routes():
    import urllib
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            "endpoint": rule.endpoint,
            "methods": list(rule.methods),
            "url": urllib.parse.unquote(str(rule))
        })
    return jsonify(routes)

# Rotas para People
@app.route('/people', methods=['GET'])
def get_all_people():
    people_list = People.query.all()
    results = [person.__dict__ for person in people_list]
    for person in results:
        person.pop('_sa_instance_state', None)
    return jsonify(results)

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get(people_id)
    if not person:
        return jsonify({"error": "Person not found", "status": 404}), 404
    result = person.__dict__
    result.pop('_sa_instance_state', None)
    return jsonify(result)

@app.route('/people', methods=['POST'])
def create_person():
    data = request.get_json()
    new_person = People(
        name=data['name'],
        height=data['height'],
        mass=data['mass'],
        hair_color=data['hair_color'],
        skin_color=data['skin_color'],
        eye_color=data['eye_color'],
        birth_year=data['birth_year'],
        gender=data['gender']
    )
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"msg": "People created successfully!", "id": new_person.id}), 201

@app.route('/people/<int:people_id>', methods=['DELETE'])
def delete_person(people_id):
    person = People.query.get(people_id)
    if not person:
        return jsonify({"msg": "Person not found"}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({"msg": "Person deleted successfully!"})

@app.route('/people/<int:people_id>', methods=['PUT'])
def update_person(people_id):
    person = People.query.get(people_id)
    if not person:
        return jsonify({"msg": "Person not found"}), 404
    data = request.get_json()
    person.name = data.get('name', person.name)
    person.height = data.get('height', person.height)
    person.mass = data.get('mass', person.mass)
    person.hair_color = data.get('hair_color', person.hair_color)
    person.skin_color = data.get('skin_color', person.skin_color)
    person.eye_color = data.get('eye_color', person.eye_color)
    person.birth_year = data.get('birth_year', person.birth_year)
    person.gender = data.get('gender', person.gender)
    db.session.commit()
    return jsonify({"msg": "Person updated successfully!"})


# Rotas para Planets
@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    results = [planet.__dict__ for planet in planets]
    for planet in results:
        planet.pop('_sa_instance_state', None)
    return jsonify(results)

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planet not found", "status": 404}), 404
    result = planet.__dict__
    result.pop('_sa_instance_state', None)
    return jsonify(result)

@app.route('/planets', methods=['POST'])
def create_planet():
    data = request.get_json()
    new_planet = Planet(
        name=data['name'],
        climate=data['climate'],
        terrain=data['terrain'],
        population=data['population']
    )
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({"msg": "Planet created successfully!", "id": new_planet.id}), 201

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"msg": "Planet not found"}), 404
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"msg": "Planet deleted successfully!"})

# Rotas para Vehicles
@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicle.query.all()
    results = [vehicle.__dict__ for vehicle in vehicles]
    for vehicle in results:
        vehicle.pop('_sa_instance_state', None)
    return jsonify(results)


@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found", "status": 404}), 404
    result = vehicle.__dict__
    result.pop('_sa_instance_state', None)
    return jsonify(result)

@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    new_vehicle = Vehicle(
        name=data['name'],
        model=data['model'],
        manufacturer=data['manufacturer'],
        passengers=data['passengers'],
        crew=data['crew'],
        length=data['length'],
        max_atmosphering_speed=data['max_atmosphering_speed']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({"msg": "Vehicle created successfully!", "id": new_vehicle.id}), 201

@app.route('/vehicles/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({"msg": "Vehicle not found"}), 404
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"msg": "Vehicle deleted successfully!"})

@app.route('/vehicles/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({"msg": "Vehicle not found"}), 404
    data = request.get_json()
    vehicle.name = data.get('name', vehicle.name)
    vehicle.model = data.get('model', vehicle.model)
    vehicle.manufacturer = data.get('manufacturer', vehicle.manufacturer)
    vehicle.passengers = data.get('passengers', vehicle.passengers)
    vehicle.crew = data.get('crew', vehicle.crew)
    vehicle.length = data.get('length', vehicle.length)
    vehicle.max_atmosphering_speed = data.get('max_atmosphering_speed', vehicle.max_atmosphering_speed)
    db.session.commit()
    return jsonify({"msg": "Vehicle updated successfully!"})


# Rotas para Users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    results = [user.__dict__ for user in users]
    for user in results:
        user.pop('_sa_instance_state', None)
    return jsonify(results)

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user_id = request.headers.get('user_id')
    if not user_id:
        return jsonify({"msg": "User ID is required"}), 400
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    results = [fav.__dict__ for fav in favorites]
    for fav in results:
        fav.pop('_sa_instance_state', None)
    return jsonify(results)

# Rotas para Favoritos
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = request.headers.get('user_id')
    if not user_id:
        return jsonify({"msg": "User ID is required"}), 400
    existing_favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if existing_favorite:
        return jsonify({"msg": "Planet is already in favorites"}), 400
    favorite = Favorite(user_id=user_id, planet_id=planet_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"msg": "Planet added to favorites!"}), 201

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user_id = request.headers.get('user_id')
    if not user_id:
        return jsonify({"msg": "User ID is required"}), 400
    existing_favorite = Favorite.query.filter_by(user_id=user_id, people_id=people_id).first()
    if existing_favorite:
        return jsonify({"msg": "Person is already in favorites"}), 400
    favorite = Favorite(user_id=user_id, people_id=people_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"msg": "Person added to favorites!"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
