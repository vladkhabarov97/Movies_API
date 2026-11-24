from http.client import responses

import pytest
import  requests

import config.credentials
from clients.auth_api import AuthApi
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
def creating_movie(authenticated_super_admin):
    payload = get_movie_payload()
    response = authenticated_super_admin.movies_api.create_movie(payload)
    return response.json()
