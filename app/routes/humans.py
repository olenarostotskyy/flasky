from app import db
from app.models.humans import Human
from flask import Blueprint, jsonify, make_response,request,abort, Response
from app.models.cats import Cat

humans_bp=Blueprint("humans",__name__,url_prefix="/humans")

@humans_bp.route("",methods=["POST"])
def create_human():
    request_body= request.get_json()
    new_human = Human(
        name=request_body["name"])

    db.session.add(new_human)
    db.session.commit()
    return make_response(f"Human {new_human.id} is created",201)


@humans_bp.route("",methods=["GET"])
def get_all_humans():

    humans=Human.query.all()  

    human_response=[]
    for human in humans:
        human_response.append(
            {
            "id":human.id,
            "name": human.name
            }
        )
    return make_response(jsonify(human_response),200 )

def valid_human(human_id):
    try:
        human_id=int(human_id)
    except:
        abort(make_response({"msg":f"invalid id {human_id}"},400)  ) 

    human=Human.query.get(human_id)    
    
    if not human:
        abort(make_response({"msg":f"no human with id {human_id}"},404)  ) 
    return human


@humans_bp.route("/<human_id>/cats",methods=["POST"]) 
def create_cat(human_id):
     human=valid_human(human_id)
     request_body= request.get_json()

     new_cat=Cat(
         name=request_body["name"],
         color=request_body["color"],
         age=request_body["age"],
         human=human
     )
    
     db.session.add(new_cat)
     db.session.commit()

     return{
         "msg":f"new cat {new_cat.name} created for {human.name}"
     }, 201

@humans_bp.route("/<human_id>/cats",methods=["GET"])
def get_cats(human_id):
    human=valid_human(human_id)

    rsp=[]
    for cat in human.cats:
        rsp.append({
            "id":cat.id,
            "name":cat.name,
            "color":cat.color,
            "age": cat.age
        })
    return jsonify(rsp),200
