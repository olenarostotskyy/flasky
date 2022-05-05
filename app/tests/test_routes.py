from app.models.cats import Cat
def test_get_all_cats_with_no_records(client):
    # Act
    response = client.get("/cats")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_one_cat(client, seven_cats)   :
     response = client.get("/cats/1")
     response_body = response.get_json()

     assert response.status_code == 200
     assert response_body == {
         "id":1,
         "name":"Jazz",
         "color":"black",
         "age":"8"}

def test_get_all_cats_list(client,seven_cats):
    # Act
    response = client.get("/cats")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body)==7
     

def test_get_one_cat_with_empty_db_returns_404(client):
    response = client.get("/cats/1")

    assert response.status_code ==404



def test_post_one_cat_creats_cat_in_db(client):
    response = client.post('/cats', json = {
        "name": "Bernie", "age":"14", "color":"grey"})
    #response_body = response.get_json()

    assert response.status_code == 201
    assert response.get_data()==b"Cat 1 is created"

    print(response.get_data())

    cats = Cat.query.all()
    assert len(cats) == 1
    assert cats[0].name == "Bernie"
    assert cats[0].age == "14"
    assert cats[0].color == "grey"
