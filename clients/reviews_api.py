from custom_requester.custom_requester import CustomRequester
from config.base_urls import API_BASE_URL

class ReviewsApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=API_BASE_URL)

    def get_reviews(self, movie_id, expected_status=200, **kwargs):
        return self.send_request(
            method="GET",
            endpoint=f"/movies/{movie_id}/reviews",
            expected_status=expected_status,
            **kwargs
        )

    def create_review(self, movie_id, data: dict, expected_status=201, **kwargs):
        return self.send_request(
            method="POST",
            endpoint=f"/movies/{movie_id}/reviews",
            data=data,
            expected_status=expected_status,
            **kwargs
        )

    def update_review(self, movie_id, data: dict, expected_status=200, **kwargs):
        return self.send_request(
            method="PUT",
            endpoint=f"/movies/{movie_id}/reviews",
            data=data,
            expected_status=expected_status,
            **kwargs
        )

    def delete_review(self, movie_id, expected_status=200, **kwargs):
        return self.send_request(
            method="DELETE",
            endpoint=f"/movies/{movie_id}/reviews",
            expected_status=expected_status,
            **kwargs
        )

    def hide_review(self, movie_id, user_id, expected_status=200, **kwargs):
        return self.send_request(
            method="PATCH",
            endpoint=f"/movies/{movie_id}/reviews/hide/{user_id}",
            expected_status=expected_status,
            **kwargs
        )

    def show_review(self, movie_id, user_id, expected_status=200, **kwargs):
        return self.send_request(
            method="PATCH",
            endpoint=f"/movies/{movie_id}/reviews/show/{user_id}",
            expected_status=expected_status,
            **kwargs
        )