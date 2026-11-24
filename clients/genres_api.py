from custom_requester.custom_requester import CustomRequester
from config.base_urls import API_BASE_URL

class GenresApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=API_BASE_URL)

    def get_genres_list(self, expected_status=200, **kwargs):
        return self.send_request(
            method="GET",
            endpoint="/genres",
            expected_status=expected_status,
            **kwargs
        )

    def create_genre(self, data: dict, expected_status=201, **kwargs):
        return self.send_request(
            method="POST",
            endpoint="/genres",
            data=data,
            expected_status=expected_status,
            **kwargs
        )

    def get_genre(self, genre_id, expected_status=200, **kwargs):
        return self.send_request(
            method="GET",
            endpoint=f"/genres/{genre_id}",
            expected_status=expected_status,
            **kwargs
        )


    def delete_genre(self, genre_id, expected_status=200, **kwargs):
        return self.send_request(
            method="DELETE",
            endpoint=f"/genres/{genre_id}",
            expected_status=expected_status,
            **kwargs
        )