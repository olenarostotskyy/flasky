import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.cats import Cat


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()        

@pytest.fixture
def seven_cats(app):
    jazz = Cat(id=1, name="Jazz",color="black", age="8")
    lili = Cat(id=2, name="Lili",color="black", age="6")
    rich= Cat(id=3, name="Rich",color="green", age="1")
    diva= Cat(id=4, name="Diva",color="gray", age="1")
    marichka=Cat(id=5, name="Marichka",color="gray", age="12")
    chichi=Cat(id=6, name="Chichi",color="white", age="5")
    rob=Cat(id=7, name="Rob",color="orange", age="2")

    db.session.add_all([jazz,lili, rich, diva,marichka,chichi,rob])

    db. session.commit()

