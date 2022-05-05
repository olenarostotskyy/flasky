from json import load
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from dotenv import load_dotenv
import os




db = SQLAlchemy() #creating ogjects 
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "TESTING_DATABASE_ALCHEMY")




    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # if testing is None:
    #     app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('TESTING_SQLALCHEMY_DATABASE')
    # else:
    #     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') #postgresql+psycopg2://postgres:postgres@localhost:5432/cats_development'
    #     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)# initialize sqlalchemy ogject
    migrate.init_app(app, db)

    from .models.cats import Cat

    from.routes.cats import cats_bp
    app.register_blueprint(cats_bp)

    return app