from page_objects.base_page import BasePage
from page_objects.locators import InternalPagesLocators


class InternalPage(BasePage):
    @property
    def active_menu(self):
        return self.find_element(InternalPagesLocators.ACTIVE_MENU)

    @property
    def user_menu(self):
        return self.find_element(InternalPagesLocators.USER_MENU)


    def initiate_sigh_in(self):
        """ Initiate Sign in (click to Sign in menu) """
        el_sign_in = self.find_element(InternalPagesLocators.SIGN_IN)
        el_sign_in.click()

    def logout(self):
        """ Logout (Sign out) at Oxwall site """
        if self.is_element_present(InternalPagesLocators.USER_MENU):
            self.actions.move_to_element(self.user_menu)
            self.actions.perform()
            el_sign_out = self.find_element(InternalPagesLocators.SIGN_OUT)
            el_sign_out.click()
