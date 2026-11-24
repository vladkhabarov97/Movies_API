from utils.data_generator import DataGenerator


def test_update_review(creating_movie, authenticated_user):

    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    authenticated_user.reviews_api.create_review(movie_id=movie_id, data=data)
    new_data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    response = authenticated_user.reviews_api.update_review(movie_id=movie_id, data=new_data)

    assert response.status_code == 200
    assert response.json()["rating"] == new_data["rating"]
    assert response.json()["text"] == new_data["text"]

def test_update_review_not_found(creating_movie, authenticated_user):
    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    authenticated_user.reviews_api.create_review(movie_id=movie_id, data=data)
    authenticated_user.reviews_api.delete_review(movie_id=movie_id)
    new_data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    response = authenticated_user.reviews_api.update_review(movie_id=movie_id, data=new_data, expected_status=404)

    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"