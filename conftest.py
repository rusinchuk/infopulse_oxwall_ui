import pytest
from selenium import webdriver
from oxwall_app import OxwallApp


@pytest.fixture()
def driver():
    # Open site
    driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver_win32\chromedriver.exe")
    return driver


@pytest.fixture()
def app(driver):
    base_url = "https://demo.oxwall.com"
    return OxwallApp(driver, base_url)


@pytest.fixture()
def login_user(app):
    username = "demo"
    password = "demo"
    app.login(username, password)
    yield username
    app.logout()
