def test_delete_movie(authenticated_super_admin, creating_movie):

    movie_id = creating_movie["id"]
    response = authenticated_super_admin.movies_api.delete_movie(movie_id=movie_id)

    assert response.status_code == 200

def test_delete_movie_unauthenticated(unauthenticated_api_manager, creating_movie):

    movie_id = creating_movie["id"]
    response = unauthenticated_api_manager.movies_api.delete_movie(movie_id=movie_id, expected_status=401)

    assert response.status_code == 401
    assert "message" in response.json()

def test_delete_movie_unfound(authenticated_super_admin):

    response = authenticated_super_admin.movies_api.delete_movie(movie_id=0, expected_status=404)

    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"

