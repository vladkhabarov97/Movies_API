from utils.data_generator import DataGenerator


def test_hide_review(creating_movie, authenticated_super_admin):

    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    create_response = authenticated_super_admin.reviews_api.create_review(movie_id=movie_id, data=data)
    user_id = create_response.json()["userId"]
    authenticated_super_admin.reviews_api.hide_review(movie_id=movie_id, user_id=user_id)
    response = authenticated_super_admin.reviews_api.show_review(movie_id=movie_id, user_id=user_id)

    assert response.status_code == 200

def test_hide_review_not_found(creating_movie, authenticated_super_admin):

    movie_id = creating_movie["id"]
    data = {"rating": DataGenerator.generate_random_rating(), "text": DataGenerator.generate_random_description()}
    create_response = authenticated_super_admin.reviews_api.create_review(movie_id=movie_id, data=data)
    user_id = create_response.json()["userId"]
    authenticated_super_admin.reviews_api.delete_review(movie_id=movie_id)
    response = authenticated_super_admin.reviews_api.show_review(movie_id=movie_id, user_id=user_id, expected_status=404)

    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["error"] == "Not Found"