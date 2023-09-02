"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template
from models import db,connect_db,Cupcake


app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = '123'
app.config['DEBUG_TB_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

@app.route('/')
def index():
    cups = Cupcake.query.all()
    return render_template('index.html', cups=cups)

@app.route('/api/cupcakes')
def get_cupcakes():
    """get data of all cupcakes"""
    cups = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cups]
    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """get data for specific cupcake"""
    
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """create cupcake with data from request"""
    new_cupcake = Cupcake(flavor = request.json.get('flavor'), size = request.json.get('size'), rating = request.json.get('rating'), image = request.json.get('image'))
    db.session.add(new_cupcake)
    db.session.commit()
    resp_json = jsonify(cupcake=new_cupcake.serialize())
    return (resp_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_todo(id):
    cupcake = Cupcake.query.get_or_404(id)
   
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)    
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted") 
