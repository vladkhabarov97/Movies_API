def test_get_movie(api_manager, creating_movie):

    movie_id = creating_movie["id"]
    response = api_manager.movies_api.get_movie(movie_id=movie_id)

    assert response.status_code == 200

def test_get_movie_invalid(api_manager):

    response = api_manager.movies_api.get_movie(movie_id=1, expected_status=404)

    assert response.status_code == 404