from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name=db.Column(db.String(20), nullable=False)
    last_name=db.Column(db.String(20), nullable=False)
    dob=db.Column(db.String(10), nullable = False)
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'dob': self.dob        
}
class StarRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    def __repr__(self):
        return f'<StarRating {self.rating}>' 

    def serialize(self):
        return {
                "id": self.id,
                "rating": self.rating,
            }
class ExoticWeapon(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        weapon_name=db.Column(db.String(120), nullable=False)
        weapon_type=db.Column(db.String(20), nullable=False)
        weapon_class=db.Column(db.String(20), nullable=False)
        weapon_lore=db.Column(db.String(1000), nullable=False)
        location_description=db.Column(db.String(1000), nullable=False)
        location_video=db.Column(db.String(200), nullable=True)
        weapon_Img =db.Column(db.String(200), nullable=False)

        def __repr__(self):
            return f'<ExoticWeapon {self.weapon_name}>' 

        def serialize(self):
            return {
                "id": self.id,
                "weapon_name": self.weapon_name,
                "weapon_type": self.weapon_type,
                "weapon_class": self.weapon_class,
                "weapon_lore": self.weapon_lore,
                "location_description": self.location_description,
                "location_video": self.location_video,
                "weapon_Img": self.weapon_Img, 
            }
class LegendaryWeapon(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        weapon_name=db.Column(db.String(120), nullable=False)
        weapon_type=db.Column(db.String(20), nullable=False)
        weapon_class=db.Column(db.String(20), nullable=False)
        weapon_lore=db.Column(db.String(1000), nullable=False)
        location_description=db.Column(db.String(1000), nullable=True)
        location_video=db.Column(db.String(200), nullable=True)
        weapon_Img =db.Column(db.String(200), nullable=False) 


        def __repr__(self):
            return f'<Legendaryweapon {self.weapon_name}>' 

        def serialize(self):
            return {
                "id": self.id,
                "weapon_name": self.weapon_name,
                "weapon_type": self.weapon_type,
                "weapon_class": self.weapon_class,
                "weapon_lore": self.weapon_lore,
                "location_description": self.location_description,
                "location_video": self.location_video,
                "weapon_Img": self.weapon_Img,

            }
class RareWeapon(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        weapon_name=db.Column(db.String(120), nullable=False)
        weapon_type=db.Column(db.String(20), nullable=False)
        weapon_class=db.Column(db.String(20), nullable=False)
        weapon_lore=db.Column(db.String(1000), nullable=False)
        location_description=db.Column(db.String(1000), nullable=True)
        location_video=db.Column(db.String(200), nullable=True)
        weapon_Img =db.Column(db.String(200), nullable=False) 

# FINISHED WEAPON IMAGE AND LOCATION IMAGE, NEED TO FIND ALL THE LOCATION IMAGES
        def __repr__(self):
            return f'<Rareweapon {self.weapon_name}>' 

        def serialize(self):
            return {
                "id": self.id,
                "weapon_name": self.weapon_name,
                "weapon_type": self.weapon_type,
                "weapon_class": self.weapon_class,
                "weapon_lore": self.weapon_lore,
                "location_description": self.location_description,
                "location_video": self.location_video,
                "weapon_Img": self.weapon_Img,


            }
class UncommonWeapon(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        weapon_name=db.Column(db.String(120), nullable=False)
        weapon_type=db.Column(db.String(20), nullable=False)
        weapon_class=db.Column(db.String(20), nullable=False)
        weapon_lore=db.Column(db.String(1000), nullable=False)
        location_description=db.Column(db.String(1000), nullable=True)
        location_video=db.Column(db.String(200), nullable=True)
        weapon_Img =db.Column(db.String(200), nullable=False) 


        def __repr__(self):
            return f'<Uncommonweapon {self.weapon_name}>' 

        def serialize(self):
            return {
                "id": self.id,
                "weapon_name": self.weapon_name,
                "weapon_type": self.weapon_type,
                "weapon_class": self.weapon_class,
                "weapon_lore": self.weapon_lore,
                "location_description": self.location_description,
                "location_video": self.location_video,
                "weapon_Img": self.weapon_Img,


            }
            # MIGHT NOT nEED A LOCATION IMAGE, MAYBE A LINK TO A GUIDE TO GEtTING THE WEApON???
