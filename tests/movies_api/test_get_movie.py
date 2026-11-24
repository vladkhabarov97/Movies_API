def test_get_movie(api_manager, creating_movie):

    movie_id = creating_movie["id"]
    response = api_manager.movies_api.get_movie(movie_id=movie_id)

    assert movie_id == response.json()["id"]

def test_get_movie_invalid(api_manager, creating_movie, authenticated_super_admin):

    movie_id = creating_movie["id"]
    authenticated_super_admin.movies_api.delete_movie(movie_id=movie_id)
    response = api_manager.movies_api.get_movie(movie_id=movie_id, expected_status=404)

    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"