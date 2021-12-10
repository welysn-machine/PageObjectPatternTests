from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, context):
        self.driver = context.driver

        # left side menu locators

        self.dashboard_button = (By.XPATH, "//span[text()='Dashboard']")
        self.book_a_consultation_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.my_consultations_button = (By.XPATH, "//span[text()='My Consultations']")
        self.learning_centre_button = (By.XPATH, "//span[text()='Learning Centre']")
        self.assessments_button = (By.XPATH, "//span[text()='Assessments']")
        self.messages_button = (By.XPATH, "//span[text()='Messages']")
        self.wellbeing_tracker_button = (By.XPATH, "//span[text()='Wellbeing Tracker']")
        self.my_account_button = (By.XPATH, "//span[text()='My Account']")
        self.settings_button = (By.XPATH, "//span[text()='Settings']")
        self.terms_and_conditions_button = (By.XPATH, "//span[text()='Terms & Conditions']")
        self.logout_button = (By.XPATH, "//span[text()='Logout']")
        self.how_it_works_button = (By.XPATH, "//span[text()='How it works']")
        self.faq_button = (By.XPATH, "//span[text()='FAQ']")
        self.welcome_tag = (By.XPATH, "//span[text()='Dashboard']")
        self.twillio_popup = (By.CLASS_NAME, 'Twilio-Icon-Content')

    def close_twillio_popup(self):
        self.driver.find_element(*self.twillio_popup).click()

    def clicking_book_a_consultation_button(self):
        self.driver.find_element(*self.book_a_consultation_button).click()

    def clicking_my_consultations_button(self):
        self.driver.find_element(*self.my_consultations_button).click()

    def clicking_dashboard_button(self):
        self.driver.find_element(*self.dashboard_button).click()

    def clicking_learning_centre_button(self):
        self.driver.find_element(*self.learning_centre_button).click()

    def clicking_assessments_button(self):
        self.driver.find_element(*self.assessments_button).click()

    def clicking_messages_button(self):
        self.driver.find_element(*self.messages_button).click()

    def clicking_wellbeing_tracker_button(self):
        self.driver.find_element(*self.wellbeing_tracker_button).click()

    def clicking_my_account_button(self):
        self.driver.find_element(*self.my_account_button).click()

    def clicking_settings_button(self):
        self.driver.find_element(*self.settings_button).click()

    def clicking_terms_and_conditions_button(self):
        self.driver.find_element(*self.terms_and_conditions_button).click()

    def clicking_logout_button(self):
        self.driver.find_element(*self.logout_button).click()

    def clicking_how_it_works_button(self):
        self.driver.find_element(*self.how_it_works_button).click()

    def clicking_faq_button(self):
        self.driver.find_element(*self.faq_button).click()

    def is_welcome_tag_displayed(self):
        return self.driver.find_element(*self.welcome_tag).is_displayed()
