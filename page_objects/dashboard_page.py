from selenium.webdriver.common.by import By

from custom_waits import present_of_elements_in_amount
from page_objects.base_page import BasePage
from page_objects.internal_page import InternalPage
from page_objects.locators import DashboardPageLocators
from page_objects.blocks.post import PostBlock


class DashboardPage(InternalPage):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.posts = self.find_elements(DashboardPageLocators.POST_BLOCK)
    #     self.post_textfield = self.find_element(DashboardPageLocators.POST_TEXTFIELD)
    #     self.send = self.find_element(DashboardPageLocators.SEND_BT)

    def is_this_page(self):
        return self.active_menu.text == "DASHBOARD"

    @property
    def posts(self):
        """ Returns a list of elements of posts located at Oxwall current page"""
        # post = PostBlock(self.find_element(DashboardPageLocators.POST_BLOCK))
        # posts = []
        # for el in self.find_elements(DashboardPageLocators.POST_BLOCK):
        #     posts.append(PostBlock(el))
        return [PostBlock(el) for el in self.find_elements(DashboardPageLocators.POST_BLOCK)]

    @property
    def post_textfield(self):
        return self.find_element(DashboardPageLocators.POST_TEXTFIELD)

    @property
    def send_button(self):
        return self.find_visible_element(DashboardPageLocators.SEND_BT)

    def create_post(self, input_text):
        """ Create a new text post
        input_text - text of new post
        """
        # self.actions.move_to_element(self.post_textfield)
        # self.actions.click()
        # self.actions.perform()

        self.post_textfield.clear()
        self.post_textfield.send_keys(input_text)
        self.send_button.click()

    def wait_new_post_appear(self, old_number):
        """ Wait until new post will appear. That means that amount of post will be it will
         wait until the quantity of post will be one more from the given number
         old_number - quantity of post before
         Returns a list of elements of posts located
         """
        return self.wait.until(
            present_of_elements_in_amount(DashboardPageLocators.POST_BLOCK, old_number + 1),
            message=f"Can't find {old_number + 1} Post block "
        )
