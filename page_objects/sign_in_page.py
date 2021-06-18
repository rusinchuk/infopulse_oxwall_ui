from page_objects.base_page import BasePage
from page_objects.locators import SignInPageLocators, InternalPagesLocators
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(BasePage):
    def is_this_page(self):
        if self.is_element_present(SignInPageLocators.SIGN_IN_WINDOW):
            return True
        else:
            return False

    def input_username(self, username):
        el_login = self.find_element(SignInPageLocators.USER_FIELD)
        el_login.clear()
        el_login.send_keys(username)

    def input_password(self, password):
        el_password = self.find_element(SignInPageLocators.PSWD_FIELD)
        el_password.clear()
        el_password.send_keys(password)

    def signin_click(self):
        el_authentication = self.find_element(SignInPageLocators.SINGIN_BT)
        el_authentication.click()

    def submit(self):
        pass

    def wait_authentication(self):
        self.wait.until(
            EC.visibility_of_element_located(InternalPagesLocators.USER_MENU),
            message="Can't find visible user menu"
        )
