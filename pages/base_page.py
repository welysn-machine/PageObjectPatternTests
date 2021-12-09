from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, context):

        self.driver = context.driver

        # left side menu locators

        self.dashboard_button = (By.XPATH, "//span[text()='Dashboard']")
        self.book_a_consultation_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.learning_centre_button = (By.XPATH, "//span[text()='Learning Centre']")
        self.assessments_button = (By.XPATH, "//span[text()='']")
        self.messages_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.wellbeing_tracker_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.my_account_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.settings_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.terms_and_conditions_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.logout_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.how_it_works_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.faq_button = (By.XPATH, "//span[text()='Book a consultation']")
        self.welcome_tag = (By.XPATH, "//span[text()='Dashboard']")

    def clicking_book_a_consultation_button(self):
        self.driver.find_element(*self.book_a_consultation_button).click()

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

    def clicking_terms_and_conditoins_button(self):
        self.driver.find_element(*self.terms_and_conditions_button).click()

    def clicking_logout_button(self):
        self.driver.find_element(*self.logout_button).click()

    def clicking_how_it_works_button(self):
        self.driver.find_element(*self.how_it_works_button).click()

    def clicking_faq_button(self):
        self.driver.find_element(*self.faq_button).click()

    def is_welcome_tag_displayed(self):
        return self.driver.find_element(*self.welcome_tag).is_displayed()