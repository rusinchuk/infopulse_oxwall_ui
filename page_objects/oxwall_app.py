from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from custom_waits import present_of_elements_in_amount
from page_objects import locators
from page_objects.dashboard_page import DashboardPage
from page_objects.main_page import MainPage
from page_objects.sign_in_page import SignInPage


class OxwallApp:
    """ Class for interaction with Oxwall web-interface"""
    def __init__(self, driver, base_url):
        self.driver = driver
        self.open(base_url)
        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        # TODO other pages

    def open(self, base_url):
        """ Open Oxwall at a given url"""
        self.driver.get(base_url)

    def login(self, username, password):
        """ Login (Sign in) to Oxwall site using a given credential of user
        :Args:
        username - username of user
        password - password of user
        """
        self.main_page.initiate_sigh_in()
        self.sign_in_page.input_username(username)
        self.sign_in_page.input_password(password)
        self.sign_in_page.signin_click()
        self.sign_in_page.wait_authentication()

    # TODO: move to page objects
    def is_element_present(self, by, locator):
        """ Check that an element is present on current Oxwall page"""
        try:
            self.driver.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True

    def logout(self):
        """ Logout (Sign out) at Oxwall site """
        if self.is_element_present(By.CLASS_NAME, "ow_console_dropdown_hover"):
            el_user_menu = self.driver.find_element(By.CLASS_NAME, "ow_console_dropdown_hover")
            self.main_page.actions.move_to_element(el_user_menu)
            self.main_page.actions.perform()
            el_sign_out = self.driver.find_element(By.XPATH, "//a[contains(@href, 'sign-out')]")
            el_sign_out.click()

    def posts(self):
        """ Returns a list of elements of posts located at Oxwall current page"""
        return self.driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")

    def create_post(self, input_text):
        """ Create a new text post
        input_text - text of new post
        """
        el_input_field = self.driver.find_element(By.CSS_SELECTOR, ".ow_newsfeed_status_input")
        el_input_field.clear()
        el_input_field.send_keys(input_text)
        el_post = self.driver.find_element(By.NAME, "save")
        el_post.click()

    def wait_new_post_appear(self, old_number):
        """ Wait until new post will appear. That means that amount of post will be it will
         wait until the quantity of post will be one more from the given number
         old_number - quantity of post before
         Returns a list of elements of posts located
         """
        return self.main_page.wait.until(
            present_of_elements_in_amount((By.CLASS_NAME, "ow_newsfeed_item"), old_number + 1),
            message=f"Can't find {old_number + 1} Post block "
        )
