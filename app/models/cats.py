from turtle import color
from unicodedata import name
from app import db 

class Cat(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    age = db.Column(db.String)
    color = db.Column(db.String)


  