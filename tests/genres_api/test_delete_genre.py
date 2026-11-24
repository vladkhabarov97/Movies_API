from utils.data_generator import DataGenerator

def test_delete_genre(authenticated_super_admin):

    genre_data = {"name": DataGenerator.generate_random_name()}
    create_response = authenticated_super_admin.genres_api.create_genre(data=genre_data)
    genre_id = create_response.json()["id"]
    response = authenticated_super_admin.genres_api.delete_genre(genre_id=genre_id)

    assert response.status_code == 200

def test_delete_genre_unauthenticated(unauthenticated_api_manager):

    get_list_response = unauthenticated_api_manager.genres_api.get_genres_list()
    genre_id = get_list_response.json()[0].get("id")
    response = unauthenticated_api_manager.genres_api.delete_genre(genre_id=genre_id, expected_status=401)

    assert response.status_code == 401
    assert "message" in response.json()

def test_delete_genre_unfound(authenticated_super_admin):

    genre_data = {"name": DataGenerator.generate_random_name()}
    create_response = authenticated_super_admin.genres_api.create_genre(data=genre_data)
    genre_id = create_response.json()["id"]
    authenticated_super_admin.genres_api.delete_genre(genre_id=genre_id)
    response = authenticated_super_admin.genres_api.delete_genre(genre_id=genre_id, expected_status=404)

    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"