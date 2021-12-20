from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


class AssessmentPage(LoginPage):
    def __init__(self, context):
        self.driver = context.driver
        super().__init__(context)

        self.begin_assessment_radio_button_rcads_child = (
            By.CSS_SELECTOR, "button[data-testid*='begin-assessment-RCADS-Child']")
        self.worry_about_things_radio_button = (By.CSS_SELECTOR, "input[name*='251'][value*='Always']")
        self.feel_sad_or_empty_radio_button = (By.CSS_SELECTOR, "input[name*='252'][value='Always']")
        self.nothing_is_fun_anymore_radio_button = (By.CSS_SELECTOR, "input[name*='256'][value='Always']")
        self.have_trouble_sleeping_radio_button = (By.CSS_SELECTOR, "input[name*='261'][value='Always']")
        self.problems_with_appetite_radio_button = (By.CSS_SELECTOR, "input[name*='265'][value='Always']")
        self.send_assessment_radio_button = (By.XPATH, "//span[text()='Send Assessment']")
        self.assessment_completed_snackbar = (By.CSS_SELECTOR, "div[data-testid='assessment-completed-snackbar']")
        self.book_now_button = (By.XPATH, "//span[text()='Book Now']")
        self.book_an_appointment_page = (By.ID, 'booking-app')

    def click_begin_assessment_button_rcads_child(self):
        self.driver.find_element(*self.begin_assessment_radio_button_rcads_child).click()

    def click_worry_about_things_radio_button(self):
        self.driver.find_element(*self.worry_about_things_radio_button).click()

    def click_feel_sad_or_empty_radio_button(self):
        self.driver.find_element(*self.feel_sad_or_empty_radio_button).click()

    def click_nothing_is_fun_anymore_radio_button(self):
        self.driver.find_element(*self.nothing_is_fun_anymore_radio_button).click()

    def click_have_trouble_sleeping_radio_button(self):
        self.driver.find_element(*self.have_trouble_sleeping_radio_button).click()

    def click_problems_with_appetite_radio_button(self):
        self.driver.find_element(*self.problems_with_appetite_radio_button).click()

    def click_send_assessment_radio_button(self):
        self.driver.find_element(*self.send_assessment_radio_button).click()

    def assessment_completed_snackbar_button_displayed(self):
        return self.driver.find_element(*self.assessment_completed_snackbar).is_displayed()

    def click_book_now_button(self):
        self.driver.find_element(*self.book_now_button).click()

    def book_an_appointment_page_displayed(self):
        return self.driver.find_element(*self.book_an_appointment_page).is_displayed()
