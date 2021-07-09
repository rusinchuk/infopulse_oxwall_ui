from page_objects.internal_page import InternalPage


class JoinPage(InternalPage):
    def input_username(self):
        pass


if __name__ == '__main__':
    from selenium import webdriver
    dr = webdriver.Chrome()
    dr.get("http://127.0.0.1/oxwall/join")
    join_page = JoinPage(dr)
    join_page.input_username()
