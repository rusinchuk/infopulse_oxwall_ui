from selenium.webdriver.common.by import By


class InternalPagesLocators:
    # Right menu elements:
    SIGN_IN = (By.CSS_SELECTOR, ".ow_signin_label")
    SIGN_UP = (By.CLASS_NAME, 'ow_console_item_link')
    USER_BOARD = (By.CLASS_NAME, 'ow_notification_list')
    USER_MENU = (By.CLASS_NAME, "ow_console_dropdown_hover")
    SIGN_OUT = (By.XPATH, ".//a[contains(@href, 'sign-out')]")
    USER_ICON = (By.CSS_SELECTOR, ".ow_console_items_wrap > div:nth-child(5)")
    # Left menu elements:
    ACTIVE_MENU = (By.CSS_SELECTOR, ".ow_responsive_menu .ow_main_menu .active")
    MAIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_main_menu_index a")
    DASHBOARD_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_dashboard a")
    JOIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_base_join_menu_item a")
    MEMBERS_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_users_main_menu_item a")
    PHOTO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .photo_photo a")
    VIDEO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .video_video ")


class SignInPageLocators:
    SIGN_IN_WINDOW = (By.ID, "base_cmp_floatbox_ajax_signin")
    USER_FIELD = (By.NAME, "identity")
    PSWD_FIELD = (By.NAME, "password")
    SINGIN_BT = (By.CSS_SELECTOR, ".ow_button span .ow_positive")


class DashboardPageLocators:
    POST_TEXTFIELD = (By.CLASS_NAME, "ow_newsfeed_status_input")
    POST_BLOCK = (By.CLASS_NAME, "ow_newsfeed_item")
    SEND_BT = (By.XPATH, '//input[@name="save"]')


class PostLocator:
    POST_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    LIKES_BUTTON = ()
    LIKES_COUNTER = ()
    COMMENTS_COUNTER = (By.CLASS_NAME, 'newsfeed_counter_comments')
    COMMENTS_BUTTON = ()

