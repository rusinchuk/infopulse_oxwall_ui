import json
import pytest
import configparser

from db.user_connector import OxwallDB
from page_objects.oxwall_app import OxwallApp
from value_objects.user_object import User
import os.path

PROJECT_DIR = os.path.dirname(__file__)


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json",
                     help="project config file name")


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    with open(os.path.join(PROJECT_DIR, filename)) as f:
        return json.load(f)


@pytest.fixture(scope="session")
def config_ini(request):
    filename = request.config.getoption("--config")
    conf = configparser.ConfigParser()
    with open(os.path.join(PROJECT_DIR, filename)) as f:
        conf.read_file(f)
    return conf

@pytest.fixture()
def driver(selenium):
    # Open site
    driver = selenium
    # driver.get("https://demo.oxwall.com")
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver, base_url):
    # base_url = "http://127.0.0.1/oxwall/"
    return OxwallApp(driver, base_url)


@pytest.fixture()
def admin(config):
    return User(**config["admin"])


@pytest.fixture()
def login_user(app, admin):
    user = admin
    app.login(user.username, user.password)
    yield user
    app.logout()


@pytest.fixture()
def logout(app):
    yield
    app.logout()


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(**config["db"])
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
    # TO DO
