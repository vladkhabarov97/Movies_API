from utils.data_generator import DataGenerator


def test_delete_review(creating_movie, authenticated_user):

    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    authenticated_user.reviews_api.create_review(movie_id=movie_id, data=data)
    response = authenticated_user.reviews_api.delete_review(movie_id=movie_id)

    assert response.status_code == 200

    get_response = authenticated_user.reviews_api.get_reviews(movie_id=movie_id)

    assert get_response.status_code == 200
    assert get_response.json() == []

def test_delete_review_not_found(creating_movie, authenticated_user):

    movie_id = creating_movie["id"]
    response = authenticated_user.reviews_api.delete_review(movie_id=movie_id, expected_status=404)

    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"