from page_objects.locators import PostLocator
from value_objects.user_object import User


class PostBlock:
    def __init__(self, element):
        self.element = element
        # self.wait = WebDriverWait(driver, 5)

    @property
    def text(self):
        return self.element.find_element(*PostLocator.POST_TEXT).text

    @property
    def time(self):
        return self.element.find_element(*PostLocator.POST_TIME).text

    @property
    def user(self):
        user_link = self.element.find_element(*PostLocator.POST_USER)
        real_name = user_link.text
        username = user_link.get_attribute("href").split("/")[-1]
        return User(username=username, real_name=real_name)

    @property
    def like_bt(self):
        return self.element.find_element(*PostLocator.LIKES_BUTTON)

    def delete(self):
        # TODO
        pass

    def add_like(self):
       self.like_bt.click()
