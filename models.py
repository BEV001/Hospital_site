from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Association table для связи пользователей с регионами
user_regions = db.Table('user_regions',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('region_id', db.Integer, db.ForeignKey('regions.id'))
)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(150))
    position = db.Column(db.String(100))
    regions = db.relationship('Region', secondary=user_regions, backref='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class Hospital(db.Model):
    __tablename__ = 'hospitals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    image_filename = db.Column(db.String(200))
    country = db.Column(db.String(50), default='Россия')
    region = db.Column(db.String(100))   
    city = db.Column(db.String(100))
    street_type = db.Column(db.String(50))  # шоссе, бульвар и т.д.
    street_name = db.Column(db.String(200))
    house = db.Column(db.String(50))          
    building = db.Column(db.String(50))     
    address_full = db.Column(db.String(300))  # полный адрес для удобства
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    license_lu = db.Column(db.Boolean, default=False)
    hot_beds = db.Column(db.Boolean, default=False)
    hot_beds_count = db.Column(db.Integer, default=0) 
    quotas_vmp_2025 = db.Column(db.Boolean, default=False)
    plan_lu_2025 = db.Column(db.Integer, default=0)
    sales_lu_2025 = db.Column(db.JSON, default={}) 

    # Контактные данные (один контакт для простоты)
    contact_full_name = db.Column(db.String(150))
    contact_position = db.Column(db.String(100))
    contact_phone = db.Column(db.String(50))
    contact_email = db.Column(db.String(120))
