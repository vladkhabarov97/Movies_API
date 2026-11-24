from utils.data_generator import DataGenerator


def test_get_reviews(creating_movie, authenticated_user):

    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    authenticated_user.reviews_api.create_review(movie_id=movie_id, data=data)
    response = authenticated_user.reviews_api.get_reviews(movie_id=movie_id)

    assert response.status_code == 200
    assert "userId" in response.json()[0]
    assert "rating" in response.json()[0]
    assert "text" in response.json()[0]

def test_get_reviews_not_found(creating_movie, authenticated_super_admin):

    movie_id = creating_movie["id"]
    authenticated_super_admin.movies_api.delete_movie(movie_id=movie_id)
    response = authenticated_super_admin.reviews_api.get_reviews(movie_id=movie_id, expected_status=404)

    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"