from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, context):
        self.driver = context.driver

        # left side menu locators

        self.dashboard_button = (By.XPATH, "//span[text()='Dashboard']")
        self.book_consultation_button = (By.XPATH, "//p[text()='Book a consultation']")
        self.book_psychologist_button = (By.XPATH, "//span[text()='Book a Psychologist']")
        self.book_coach_button = (By.XPATH, "//span[text()='Book a Coach']")
        self.book_manager_assistance = (By.XPATH, "//span[text()='Book Manager Assistance']")
        self.book_dietitian_button = (By.XPATH, "//span[text()='Book a Dietitian']")
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
        self.twillio_popup = (By.CSS_SELECTOR, 'div[class^""]')

    def close_twillio_popup(self):
        try:
            self.driver.find_element(*self.twillio_popup).click()
        except:
            pass

    def click_book_consultation_button(self):
        self.driver.find_element(*self.book_consultation_button).click()

    def click_book_psychologist_button(self):
        self.driver.find_element(*self.book_psychologist_button).click()

    def click_book_coach_button(self):
        self.driver.find_element(*self.book_coach_button).click()

    def click_book_manager_assistance_button(self):
        self.driver.find_element(*self.book_manager_assistance).click()

    def click_book_dietitian_button(self):
        self.driver.find_element(*self.book_dietitian_button).click()

    def click_my_consultations_button(self):
        self.driver.find_element(*self.my_consultations_button).click()

    def click_dashboard_button(self):
        self.driver.find_element(*self.dashboard_button).click()

    def click_learning_centre_button(self):
        self.driver.find_element(*self.learning_centre_button).click()

    def click_assessments_button(self):
        self.driver.find_element(*self.assessments_button).click()

    def click_messages_button(self):
        self.driver.find_element(*self.messages_button).click()

    def click_wellbeing_tracker_button(self):
        self.driver.find_element(*self.wellbeing_tracker_button).click()

    def click_my_account_button(self):
        self.driver.find_element(*self.my_account_button).click()

    def click_settings_button(self):
        self.driver.find_element(*self.settings_button).click()

    def click_terms_and_conditions_button(self):
        self.driver.find_element(*self.terms_and_conditions_button).click()

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()

    def click_how_it_works_button(self):
        self.driver.find_element(*self.how_it_works_button).click()

    def click_faq_button(self):
        self.driver.find_element(*self.faq_button).click()

    def welcome_tag_displayed(self):
        return self.driver.find_element(*self.welcome_tag).is_displayed()
