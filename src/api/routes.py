# """
# This module takes care of starting the API Server, Loading the DB and Adding the endpoints
# """
# from flask import Flask, request, jsonify, url_for, Blueprint
# from api.models import db, User, Weapon, Legendaryweapon
# from api.utils import generate_sitemap, APIException

# api = Blueprint('api', __name__)

"""

# PIPENV RUN START
# NPM RUN START

This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, StarRating, ExoticWeapon, Legendaryweapon
from api.utils import generate_sitemap, APIException

"""
JWT MODULES
"""
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = Blueprint('api', __name__)
# ITS API.ROUTE BECAUSE OF THIS LINE HERE

#LOGIN
@api.route("/signin", methods=["POST"])
def login():
    body=request.get_json()
    if 'email' not in body or body['email']=="":
        raise APIException("User Not Found", status_code=400)
    if "password" not in body or body["password"]=="":
        raise APIException("User Not Found", status_code=400)

    user=User.query.filter_by(email=body['email']).first()
    if user == None or body['password'] != user.password:
        raise APIException("User  not found or password incorrect", status_code=400)
    else:
        access_token = create_access_token(identity=body['email'])
        return jsonify(access_token=access_token)

@api.route("/protected", methods=['GET'])
@jwt_required()
def protected():
    current_user=get_jwt_identity()
    user=User.query.filter_by(email=current_user).first()
    return jsonify({"first_name":user.first_name, "email":user.email}), 200

@api.route('/signup', methods=['GET'])
def get_user():
    person=User.query.all()
    user_list=list(map(lambda x: x.serialize(), person))
    return jsonify(user_list), 200


    # HAD TO CREATE A POST FOR THE SIGN UP

@api.route('/signup', methods=['POST'])
def create_user():
    response_body= request.get_json()
    print(response_body)
    if 'email' not in response_body:
        raise APIException('bad request, email needed', status_code=400)
    if 'password' not in response_body:
        raise APIException('bad request, password needed', status_code=400)
    if 'first_name' not in response_body:
        raise APIException('bad request, first_name needed', status_code= 400)
    if 'last_name' not in response_body:
        raise APIException('bad request, last_name needed', status_code= 400)
    if 'dob' not in response_body:
        raise APIException('bad request, Date of birth needed', status_code= 400)
    new_user=User(email=response_body['email'], password=response_body['password'],first_name=response_body['first_name'],last_name=response_body['last_name'], dob=response_body['dob'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 200

@api.route('/exotics', methods=['GET'])
def exotic_get():
    weapons=ExoticWeapon.query.all()
    weapons_list=list(map(lambda x: x.serialize(), weapons))
    return jsonify(weapons_list), 200

@api.route('/exotics', methods=['POST'])
def access_exoticweapons():
    response_body = request.get_json()
    exoticWeapons=ExoticWeapon(weapon_name=response_body['weapon_name'], weapon_type=response_body['weapon_type'],weapon_class=response_body['weapon_class'], weapon_lore=response_body['weapon_lore'], location_description=response_body['location_description'])
    db.session.add(exoticWeapons)
    db.session.commit()
    return jsonify(exoticWeapons.serialize()), 200

# FIX THE READABILITY BETWEEN Exoticweapons and exoticWeapons
@api.route('/exotics/<int:exotics_id>', methods=['DELETE'])
def delexoticsId(exotics_id):
    singleweapon = ExoticWeapon.query.get(exotics_id)
    print(singleweapon)
    if singleweapon is None:
        raise APIException(
            'This Weapon doesnt exist, or has already been deleted', status_code=404)
    delete_exotics = db.session.delete(singleweapon)
    db.session.commit()
    return jsonify(singleweapon.serialize())
# CREATE A GET BY ID FOR SINGLE EXOTICS
@api.route('/exotics/<int:exotics_id>', methods=['GET'])
def getexoticsId(exotics_id):
    singleExoticweapon = ExoticWeapon.query.get(exotics_id)
    print("This is the position of a single ExoticWeapon: ", singleExoticweapon)
    return jsonify(singleExoticweapon.serialize())

# never start anything thats not a class with a captal letter
@api.route('/legendary', methods=['GET'])
def legendary_get():
    legendary_get=Legendaryweapon.query.all()
    weapons_list=list(map(lambda x: x.serialize(), legendary_get))
    return jsonify(weapons_list), 200

@api.route('/legendary', methods=['POST'])
def access_legendaryweapons():
    response_body = request.get_json()
    weaponInput=Legendaryweapon(weapon_name=response_body['weapon_name'], weapon_type=response_body['weapon_type'],weapon_class=response_body['weapon_class'], weapon_lore=response_body['weapon_lore'], location_description=response_body['location_description'])
    db.session.add(weaponInput)
    db.session.commit()
    return jsonify(weaponInput.serialize()), 200

@api.route('/legendary/<int:legendary_id>', methods=['DELETE'])
def legendaryId(legendary_id):
    singleweapon = Legendaryweapon.query.get(legendary_id)
    print(singleweapon)
    if singleweapon is None:
        raise APIException(
            'This Weapon doesnt exist, or has already been deleted', status_code=404)
    delete_legendary = db.session.delete(singleweapon)
    db.session.commit()
    return jsonify(singleweapon.serialize())


@api.route('/starrating', methods=['GET'])
def get_rating():
    rating=StarRating.query.all()
    rating_list=list(map(lambda x: x.serialize(), rating))
    return jsonify(rating_list), 200


@api.route('/starrating', methods=['POST'])
def create_rating():
    response_body = request.get_json()
    rating=StarRating(rating=response_body['rating'])
    db.session.add(rating)
    db.session.commit()
    return jsonify(rating.serialize()), 200

#     # YOU WILL DELEte bY USING THE ID IN THE URL WHEN TRYING TO DELETE IN POSTMAN

