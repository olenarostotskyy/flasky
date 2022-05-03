from app import db
from app.models.cats import Cat
from flask import Blueprint, jsonify, make_response,request,abort


# class Cat:
#     def __init__(self, id, name, age, color):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.color=color

# cats=[
#     Cat(1,"Richard",1, "yellow"),
#     Cat(2,"Simba",3,"gray"),
#     Cat(3,"Diva", 0.5, "black")
# ]  

#bulding API

cats_bp=Blueprint("cats",__name__,url_prefix="/cats")

@cats_bp.route("",methods=["GET"])
def get_all_cats():
    # building cat response
    cats=Cat.query.all()
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

@cats_bp.route("",methods=["POST"])
def create_one_cat():
    request_body= request.get_json()
    new_cat = Cat(
        name=request_body["name"],
        age=request_body ["age"], 
        color=request_body["color"])

    db.session.add(new_cat)
    db.session.commit()
    return make_response(f"Cat {new_cat.id} is created",201)
    
    # {
    #     "id":new_cat.id,
    #     "msg": f"cat {new_cat.id} is created"
    # }


#helper function to handle errors
# def validate_cat(cat_id):
# #handle invalid cat_id, return 404
#     try:
#         cat_id=int(cat_id) #converts it in int
#     except:
#         rsp={"message”:f”{cat_id} invalid cat id"  }
#         return jsonify(rsp),404
# # search for cat_id in data, return cat
#     chosen_cat = Cat.query.get(cat_id)
# # return 404 for non-existing planet
#     if chosen_cat is None:
#         rsp={"message”:f”{cat_id} not found"  }      
#         return jsonify(rsp),400


#get cat by id
@cats_bp.route("/<cat_id>",methods=["GET"])
def get_one_cat(cat_id):
    try:
        cat_id=int(cat_id) #converts it in int
    except ValueError:
        rsp={"message": f"{cat_id} invalid cat id"}
        return jsonify(rsp),404
    chosen_cat=Cat.query.get(cat_id)    
    if chosen_cat is None:
        rsp={"message”:f”{cat_id} not found" }
        return jsonify(rsp),400
        
    rsp={
            "id":chosen_cat.id,
            "name": chosen_cat.name,
            "age":chosen_cat.age,
            "color":chosen_cat.color
    }    
    return jsonify(rsp), 200



@cats_bp.route("/<cat_id>",methods=["PUT"])
def update_cat(cat_id):
    try:
      cat_id=int(cat_id)
    except ValueError:
        rsp={"msg":f"Invalid id: {cat_id}"}  
        return jsonify(rsp), 400
    chosen_cat=Cat.query.get(cat_id)
    if chosen_cat is None:
        rsp={"msg":f"Could not find cat id: {cat_id}"}  
        return jsonify(rsp), 404
    
    db.session.delete(chosen_cat)
    db.session.commit() # we need to commit changes after making changes to db
    
    return {"msg":f"Cat {chosen_cat.id} successfully updated"} ,200
    


@cats_bp.route("/<cat_id>",methods=["DELETE"])
def delete_cat(cat_id):
    try:
        cat_id=int(cat_id)
    except ValueError:
        rsp={"msg":f"Invalid id: {cat_id}"}  
        return jsonify(rsp), 400
    chosen_cat= Cat.query.get(cat_id)
    if chosen_cat is None:
        rsp={"msg":f"Could not find cat id: {cat_id}"}  
        return jsonify(rsp), 404
    
    db.session.delete(chosen_cat)
    db.session.commit() # we need to commit changes after making changes to db

    return {"msg":f"Cat {chosen_cat.id} successfully deleted"} ,200