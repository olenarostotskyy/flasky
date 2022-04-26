from crypt import methods
from turtle import color
from flask import Blueprint, jsonify


class Cat:
    def __init__(self, id, name, age, color):
        self.id=id
        self.name=name
        self.age=age
        self.color=color

cats=[
    Cat(1,"Richard",1, "yellow"),
    Cat(2,"Simba",3,"gray"),
    Cat(3,"Diva", 0.5, "black")
]  

#bulding API

cats_bp=Blueprint("cats_bp",__name__,url_prefix="/cats")

#endpoint
@cats_bp.route("",methods=["GET"])
def get_all_cats():
    # building cat response
    cat_response=[]
    for cat in cats:
        cat_response.append(
            {
            "id":cat.id,
            "name": cat.name,
            "age":cat.age,
            "color":cat.color
            }
        )
    return jsonify(cat_response)    

@cats_bp.route("/<cat_id>",methods=["GET"])
def get_one_cat(cat_id):
    try:
         cat_id=int(cat_id)
    except ValueError:
        rsp={"msg":f"invalid id :{cat_id}"}
        return jsonify(rsp), 400

    
    chosen_cat=None
    for cat in cats:
        if cat.id==cat_id:
            chosen_cat=cat
            break

    if chosen_cat is None:
        return {
            "msg":f"Could not find the cat id {cat_id} ",
        },404

    rsp={
        "id":chosen_cat.id,
        "name": chosen_cat.name,
        "age":chosen_cat.age,
        "color":chosen_cat.color
    }    
    return jsonify(rsp), 200

        