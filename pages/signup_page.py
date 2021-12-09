from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


class SignupPage(LoginPage):

    def __init__(self, context):
        self.driver = context.driver
        # my account page elements

        self.create_account_email_input = (By.ID, "id-email")
        self.create_account_phone_input = (By.ID, "id-phone")
        self.create_account_password_input = (By.ID, "id-password1")
        self.create_account_confirm_password_input = (By.ID, "id-password2")
        self.create_account_continue_button = (By.XPATH, "//span[text()='CONTINUE']")
        self.verify_phone_number_submit_button = (By.CSS_SELECTOR, 'button[type= "submit"]')

    def create_account(self, email, mobile_phone, password, confirm_password):
        self.driver.find_element(*self.create_account_email_input).send_keys(email)
        self.driver.find_element(*self.create_account_phone_input).send_keys(mobile_phone)
        self.driver.find_element(*self.create_account_password_input).send_keys(password)
        self.driver.find_element(*self.create_account_confirm_password_input).send_keys(confirm_password)
        self.driver.find_element(*self.create_account_continue_button).click()

    def verify_phone_number_submit_button_displayed(self):
        return self.driver.find_element(*self.verify_phone_number_submit_button).is_displayed()
