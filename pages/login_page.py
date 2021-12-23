from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.driver = context.driver

        self.get_started_button = (By.XPATH, "//span[text()='GET STARTED']")
        self.log_in_button = (By.XPATH, "//span[text()='LOG IN']")
        self.email_input = (By.ID, 'id-email')
        self.password_input = (By.ID, 'id-password')
        self.fail_login_message = (By.XPATH,
                                   '//p[text()="Something went wrong. Refresh the page or try again later." ]')

    def open_page(self):
        self.driver.get("https://staging.welysn.com/users/login/")

    def log_in(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.log_in_button).click()
        self.close_redeem_coupon_popup()

    def get_error_msg_fail_login(self):
        return self.driver.find_element(*self.fail_login_message).text

    def click_get_started_button(self):
        self.driver.find_element(*self.get_started_button).click()
