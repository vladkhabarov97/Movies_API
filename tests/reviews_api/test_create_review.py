from utils.data_generator import DataGenerator


def test_create_review(creating_movie, authenticated_user):

    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    response = authenticated_user.reviews_api.create_review(movie_id=movie_id, data=data)

    assert response.status_code == 201
    assert data["rating"] == response.json()["rating"]
    assert data["text"] == response.json()["text"]

def test_create_review_same_user(creating_movie, authenticated_user):

    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    authenticated_user.reviews_api.create_review(movie_id=movie_id, data=data)
    response = authenticated_user.reviews_api.create_review(movie_id=movie_id, data=data, expected_status=409)

    assert response.status_code == 409
    assert "message" in response.json()
    assert response.json()["error"] == "Conflict"

def test_create_review_not_found(creating_movie, authenticated_super_admin):

    movie_id = creating_movie["id"]
    authenticated_super_admin.movies_api.delete_movie(movie_id=movie_id)
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    response = authenticated_super_admin.reviews_api.create_review(movie_id=movie_id, data=data, expected_status=404)

    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"

def test_create_review_unauthenticated(creating_movie, unauthenticated_api_manager, authenticated_super_admin):

    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    response = unauthenticated_api_manager.reviews_api.create_review(movie_id=movie_id, data=data, expected_status=401)
    authenticated_super_admin.movies_api.delete_movie(movie_id=movie_id)

    assert response.status_code == 401
    assert "message" in response.json()