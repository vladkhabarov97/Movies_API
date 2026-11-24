def test_get_genres_list(api_manager):

    response = api_manager.genres_api.get_genres_list()

    assert len(response.json()) > 0
    assert "id" in response.json()[0]