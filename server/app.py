#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    # Query all bakeries from the database
    bakeries=Bakery.query.all()

    # Serialize each bakery using the to_dict() method
    bakeries = [bakery.to_dict() for bakery in bakeries]


    response = make_response(bakeries,
                          200
    )

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    # game = Game.query.filter(Game.id == id).first()
    bakery = Bakery.query.filter(Bakery.id==id).first()

    bakery_dict =bakery.to_dict()
    response = make_response(bakery_dict,
                             200
    )
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
     # Query all baked goods, sorted by price in descending order
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()

    # Serialize each baked good using the to_dict() method
    baked_goods = [baked_good.to_dict() for baked_good in baked_goods]

    # Create a JSON response
    response = make_response(baked_goods,
                              200
    )

    return response
    

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    # Query for the most expensive baked good
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()

    # Serialize the most expensive baked good using the to_dict() method
    most_expensive_dict = most_expensive.to_dict()

    # Create a JSON response
    response = make_response(jsonify(most_expensive_dict), 200)

    return response
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
