def test_get_movies_list(api_manager):

    response = api_manager.movies_api.get_movies_list(params={"page": 1, "pageSize": 10})

    assert "movies" in response.json()

def test_get_movies_list_invalid(api_manager):

    response = api_manager.movies_api.get_movies_list(params={"page": 1, "pageSize": 100}, expected_status=400)

    assert "message" in response.json()
    assert response.json()["error"] == "Bad Request"
