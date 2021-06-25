import json

import pytest

from db.user_connector import OxwallDB
from page_objects.oxwall_app import OxwallApp
from value_objects.user_object import User
import os.path

PROJECT_DIR = os.path.dirname(__file__)


@pytest.fixture()
def driver(selenium):
    # Open site
    driver = selenium
    # driver.get("https://demo.oxwall.com")
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    base_url = "http://127.0.0.1/oxwall/"
    return OxwallApp(driver, base_url)


@pytest.fixture()
def login_user(app):
    user = User(username="admin", password="pass", real_name="Admin")
    app.login(user.username, user.password)
    yield user
    app.logout()


@pytest.fixture(scope="session")
def db():
    param = {
        "host": 'localhost',
        "user": 'root',
        "password": 'mysql',
        "db": 'oxwall1'
    }
    db = OxwallDB(**param)
    yield db
    db.close()


file_name = os.path.join(PROJECT_DIR, "data", "user_positive.json")
with open(file_name, encoding="utf8") as f:
    users_data = json.load(f)


@pytest.fixture(params=users_data, ids=[str(u) for u in users_data])
def user(request, db):
    user = User(**request.param)
    db.create_user(user)
    yield user
    db.delete_user(user)


@pytest.fixture()
def delete_post(db):
    yield
    # TODO
