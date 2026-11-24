from data.movie_data import get_movie_payload

def test_create_movie(authenticated_super_admin):

    payload = get_movie_payload()
    response = authenticated_super_admin.movies_api.create_movie(payload)
    response_data = response.json()

    assert response_data["name"] == payload["name"]
    assert "id" in response_data

def test_create_movie_unauthenticated(unauthenticated_api_manager):

    payload = get_movie_payload()
    response = unauthenticated_api_manager.movies_api.create_movie(payload, expected_status=401)

    assert response.status_code == 401
    assert "message" in response.json()

def test_create_movie_no_name(authenticated_super_admin):

    payload = get_movie_payload()
    payload["name"] = ''
    response = authenticated_super_admin.movies_api.create_movie(payload, expected_status=400)

    assert response.status_code == 400
    assert "message" in response.json()
    assert response.json()["error"] == "Bad Request"

def test_create_movie_duplicate(authenticated_super_admin, creating_movie):

    duplicate_name = creating_movie["name"]
    payload = get_movie_payload()
    payload["name"] = duplicate_name
    response = authenticated_super_admin.movies_api.create_movie(payload, expected_status=409)

    assert response.status_code == 409
    assert "message" in response.json()
    assert response.json()["error"] == "Conflict"
