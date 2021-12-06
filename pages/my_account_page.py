from selenium.webdriver.common.by import By


class MyAccountPage:

    def __init__(self, context):
        self.driver = context.driver
        # my account page elements

        self.get_started_button = (By.XPATH, "//span[text()='GET STARTED']")
        self.log_in_button = (By.XPATH, "//span[text()='LOG IN']")
        self.email_input = (By.ID, 'id-email')
        self.password_input = (By.ID, 'id-password')
        self.create_account_email_input = (By.ID, "id-email")
        self.create_account_phone_input = (By.ID, "id-phone")
        self.create_account_password_input = (By.ID, "id-password1")
        self.create_account_confirm_password_input = (By.ID, "id-password2")
        self.create_account_continue_button = (By.XPATH, "//span[text()='CONTINUE']")
        self.welcome_tag = (By.XPATH,  "//span[text()='Dashboard']")
        self.fail_login_message = (By.XPATH,
                                   '//p[text()="Please enter a correct email and password. Note that both fields may be case-sensitive." ]')

    def open_page(self):
        self.driver.get("https://staging.welysn.com/users/login/?next=/clients/find-psychologist/")

    def log_in(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.log_in_button).click()

    def create_account(self, email, mobile_phone, password, confirm_password):
        self.driver.find_element(*self.get_started_button).click()
        self.driver.find_element(*self.create_account_email_input).send_keys(email)
        self.driver.find_element(*self.create_account_phone_input).send_keys(mobile_phone)
        self.driver.find_element(*self.create_account_password_input).send_keys(password)
        self.driver.find_element(*self.create_account_confirm_password_input).send_keys(confirm_password)
        self.driver.find_element(*self.create_account_continue_button).click()

    def is_use_tag_displayed(self):
        return self.driver.find_element(*self.welcome_tag).is_displayed()

    def get_error_msg_fail_login(self):
        return self.driver.find_element(*self.fail_login_message).text
