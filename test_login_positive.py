import time


def test_login(driver, app):
    app.main_page.initiate_sigh_in()
    assert app.sign_in_page.is_this_page()
    app.sign_in_page.input_username("demo")
    app.sign_in_page.input_password("demo")
    app.sign_in_page.signin_click()
    app.sign_in_page.wait_authentication()
    assert app.dashboard_page.active_menu.text == "DASHBOARD"
    assert app.dashboard_page.is_this_page()
