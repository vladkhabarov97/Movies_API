import pytest
import  requests
import random
import config.credentials
from clients.api_manager import ApiManager
from data.movie_data import get_movie_payload
from utils.data_generator import DataGenerator


@pytest.fixture(scope="session")
def session():
    http_session = requests.Session()
    yield http_session
    http_session.close()

@pytest.fixture(scope="session")
def api_manager(session):
    return ApiManager(session)

@pytest.fixture
def unauthenticated_api_manager(api_manager):
    session = requests.Session()
    yield ApiManager(session)
    session.close()

@pytest.fixture(scope="function")
def authenticated_super_admin(api_manager):
    api_manager.auth_api.authenticate((
        config.credentials.super_admin_email,
        config.credentials.super_admin_password
    ))
    return api_manager


@pytest.fixture(scope="function")
def authenticated_user():

    session = requests.Session()
    user_api = ApiManager(session)
    password = DataGenerator.generate_random_password()
    user_data = {
        "email": DataGenerator.generate_random_email(),
        "password": password,
        "fullName": "Test Testov",
        "passwordRepeat": password,
        "roles": ["USER"]
    }
    user_api.auth_api.register_user(user_data)
    user_api.auth_api.authenticate((user_data["email"], user_data["password"]))

    yield user_api
    session.close()

@pytest.fixture(scope="function")
def creating_movie(authenticated_super_admin, existed_genre_id):
    payload = get_movie_payload(existed_genre_id)
    response = authenticated_super_admin.movies_api.create_movie(payload)
    movie = response.json()
    yield movie

    try:
        authenticated_super_admin.movies_api.delete_movie(movie_id=movie["id"], expected_status=200)
    except ValueError:
        pass


@pytest.fixture(scope="session")
def existed_genre_id(api_manager):
    genre_list = api_manager.genres_api.get_genres_list()
    genre_id = random.choice(genre_list.json())["id"]
    return genre_id
