from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12341234@localhost/pythonAPI'
app.config['JWT_SECRET_KEY'] = 'its-jwt'  
db = SQLAlchemy(app)
jwt = JWTManager(app)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price
        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/signup', methods=['POST'])
def signup():
    if not request.json or 'username' not in request.json or 'password' not in request.json:
        abort(400)
    username = request.json['username']
    password = generate_password_hash(request.json['password'])
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    if not request.json or 'username' not in request.json or 'password' not in request.json:
        abort(400)
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


@app.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products])

@app.route('/products/<int:id>', methods=['GET'])
@jwt_required()
def get_product(id):
    product = Product.query.get(id)
    if product is None:
        abort(404)
    return jsonify(product.serialize())

@app.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    if not request.json:
        abort(400)
    product = Product(title=request.json['title'], description=request.json.get('description', ""), price=request.json['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.serialize()), 201

@app.route('/products/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    product = Product.query.get(id)
    if product is None:
        abort(404)
    if not request.json:
        abort(400)
    product.title = request.json.get('title', product.title)
    product.description = request.json.get('description', product.description)
    product.price = request.json.get('price', product.price)
    db.session.commit()
    return jsonify(product.serialize())

@app.route('/products/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    product = Product.query.get(id)
    if product is None:
        abort(404)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
