import pytest
import  requests

from config.credentials import super_admin_email, super_admin_password
from custom_requester.custom_requester import CustomRequester
from config.base_urls import AUTH_BASE_URL
from config import credentials
from clients.auth_api import AuthApi
from utils.data_generator import DataGenerator
from clients.api_manager import ApiManager

@pytest.fixture(scope="session")
def session():
    http_session = requests.Session()
    yield http_session
    http_session.close()

@pytest.fixture(scope="session")
def api_manager(session):
    return ApiManager(session)

@pytest.fixture
def unauthenticated_api_manager():
    session = requests.Session()
    yield AuthApi(session)
    session.close()

@pytest.fixture(scope="function")
def test_user():
    password = DataGenerator.generate_random_password()
    return {
        "email": DataGenerator.generate_random_email(),
        "fullName": DataGenerator.generate_random_name(),
        "password": password,
        "passwordRepeat": password,
        "roles": ["USER"]
    }

@pytest.fixture(scope="function")
def registered_user(api_manager, test_user):
    response = api_manager.auth_api.register_user(test_user).json()
    test_user["id"] = response["id"]

    return test_user

@pytest.fixture(scope="function")
def authenticated_user(api_manager):

    api_manager.auth_api.authenticate((
        super_admin_email,
        super_admin_password
    ))

    return api_manager

