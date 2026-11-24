from utils.data_generator import DataGenerator


def test_update_movie(authenticated_super_admin, creating_movie):

    movie_id = creating_movie["id"]
    old_name = creating_movie["name"]
    old_description = creating_movie["description"]
    new_data = {
            "name": DataGenerator.generate_random_name(),
            "description": DataGenerator.generate_random_description()
        }
    response = authenticated_super_admin.movies_api.update_movie(movie_id=movie_id, data=new_data)

    assert response.status_code == 200
    assert response.json()["name"] == new_data["name"]
    assert response.json()["name"] != old_name
    assert response.json()["description"] != old_description
    assert response.json()["id"] == movie_id

def test_update_movie_unfound(authenticated_super_admin, creating_movie):

    movie_id = creating_movie["id"]
    new_data = {"name": "renamed movie"}
    authenticated_super_admin.movies_api.delete_movie(movie_id=movie_id)
    response = authenticated_super_admin.movies_api.update_movie(movie_id=movie_id, data=new_data, expected_status=404)

    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"

def test_update_movie_invalid(authenticated_super_admin, creating_movie):

    movie_id = creating_movie["id"]
    new_data = {"name": 1}
    response = authenticated_super_admin.movies_api.update_movie(movie_id=movie_id, data=new_data, expected_status=400)

    assert response.status_code == 400
    assert "message" in response.json()
    assert response.json()["error"] == "Bad Request"

