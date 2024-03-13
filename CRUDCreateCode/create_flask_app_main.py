import config
# Need to do work to get the model_name and the fields accordingly in the dataclasses

def basic_context(config, model_name):
    context = f"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests
from flask import abort
from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/{config.FLASK_APP_MAIN_NAME}'
CORS(app)
db = SQLAlchemy(app)

@dataclass
class {model_name}(db.Model):
    id:int
    title:str
    image:str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200)) # change these to the appropriate fields
    image = db.Column(db.String(200))


@dataclass
class {model_name}User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/{model_name.lower()}s')
def index():
    return jsonify({model_name}.query.all()) # change for the appropriate model


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id): # this is the id of the product that we send in the request
    req = requests.get('http://docker.for.mac.localhost:8000/api/user') # this is the user service. change it accordingly--> create in config
    json = req.json()

    try:
        {model_name.lower()}User = {model_name}User(user_id=json['id'], product_id=id)
        db.session.add({model_name}User)
        db.session.commit()

        publish('{model_name.lower()}_liked', id)
    except:
        abort(400, 'You already liked this {model_name.lower()}')


    {model_name.lower()} = {model_name}.query.filter_by(id=id).first()
    if {model_name.lower()} is None:
        return jsonify({'message': '{model_name} does not exist'}), 400

    product_user = {model_name}User(user_id=1, product_id=id)
    db.session.add(product_user)
    db.session.commit()
    return jsonify({'message': 'success'}), 201 # 201 is created


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
"""