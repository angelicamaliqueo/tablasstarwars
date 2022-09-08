import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'users'
    id = Column(Integer, primary_key=True)
    password = Column(String(250))
    email = Column(String(250))
   

class Favorite_characters(Base):
    __tablename__= 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    ship_id = Column(Integer, ForeignKey('ships.id'))

class Favorite_planets(Base):
    __tablename__= 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planets_id= Column(Integer, ForeignKey('planets.id'))

class Favorite_ships(Base):
    __tablename__ = 'favorite_ships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    ships_id= Column(Integer, ForeignKey('ship.id'))

class Character(Base):
    __tablename__ = 'characters'  
    id = Column(Integer, primary_key=True)
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    eye = Column(String(250))
    birth_years = Column(String(250))
    gender = Column(String(250))

class Planets(Base):
    __tablename__ = 'planets'   
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    starship = Column(String(250))
    cost_in_credits = Column(String(250))
    lengt = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    hyperdrive_rating = Column(String(250))
    mGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))

class Ships(Base):
    __tablename__ = 'ships'  
    id = Column(Integer, primary_key=True) 
    model = Column(String(250)) 
    starship_class = Column(String(250))
    cost_in_credits = Column(String(250))
    lengt = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    hyperdrive_rating = Column(String(250))
    mGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))

     
    
 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')