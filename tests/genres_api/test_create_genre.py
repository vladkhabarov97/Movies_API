from utils.data_generator import DataGenerator

def test_create_genre(authenticated_super_admin):

    genre_data = {"name": DataGenerator.generate_random_name()}
    response = authenticated_super_admin.genres_api.create_genre(data=genre_data)

    assert "id" in response.json()
    assert genre_data["name"] == response.json()["name"]

def test_create_genre_unauthenticated(unauthenticated_api_manager):

    genre_data = {"name": DataGenerator.generate_random_name()}
    response = unauthenticated_api_manager.genres_api.create_genre(data=genre_data, expected_status=401)

    assert "message" in response.json()

def test_create_genre_invalid(authenticated_super_admin):

    genre_data = {"name": 1}
    response = authenticated_super_admin.genres_api.create_genre(data=genre_data, expected_status=400)

    assert "message" in response.json()
    assert response.json()["error"] == "Bad Request"

def test_create_genre_duplicate(authenticated_super_admin):

    genre_data = {"name": DataGenerator.generate_random_name()}
    response = authenticated_super_admin.genres_api.create_genre(data=genre_data)
    same_genre_data = {"name": response.json()["name"]}
    response = authenticated_super_admin.genres_api.create_genre(data=same_genre_data, expected_status=409)

    assert "message" in response.json()
    assert response.json()["error"] == "Conflict"

