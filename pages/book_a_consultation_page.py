from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from pages.login_page import LoginPage


class BookConsultationPage(LoginPage):

    def __init__(self, context):
        super().__init__(context)
        self.driver = context.driver

        self.book_button_list_of_available_therapists = (By.XPATH, "//span[text()='Book now']")
        self.length_of_consultation_input_radio_button = (By.ID, "standard")
        self.available_dates = (By.CSS_SELECTOR, "div[data-date='20211231']")
        self.available_time = (By.CLASS_NAME, "timeslots-picker__cell")
        self.book_button_confirm_booking = (By.XPATH, "//span[text()='BOOK']")
        self.confirmation_page = (
            By.XPATH, "//span[text()='BOOK']")
        self.available_therapists_information = (By.CSS_SELECTOR, "img[alt= 'Profile image']")
        self.filter_option = (By.XPATH, "//span[text()='Filters']")
        self.need_help_with_select_filter_options = (
            By.XPATH, "/html/body/div[3]/div[3]/form/div/div[1]/div[3]/div/div/div/div/div[1]")
        self.fears_and_phobias_select_option = (By.XPATH, "//div[text()='Fears & Phobias']")
        self.update_filter_button = (By.XPATH, "//span[text()='Update']")
        self.fears_and_phobias_button = (By.XPATH, "//span[text()='Fears & Phobias']")

    def clicking_book_button_available_therapist(self):
        self.driver.find_element(*self.book_button_list_of_available_therapists).click()

    def choosing_payment_consultation_type_and_length(self):
        self.driver.find_element(*self.length_of_consultation_input_radio_button).click()

    def setting_date_and_time(self):
        self.driver.find_element(*self.available_dates).click()
        self.driver.find_element(*self.available_time).click()

    def booking_a_consultation(self):
        self.driver.find_element(*self.book_button_confirm_booking).click()

    def confirming_consultation_is_displayed(self):
        return self.driver.find_element(*self.confirmation_page).is_displayed()

    def clicking_filter_button(self):
        self.driver.find_element(*self.filter_option).click()

    def select_filter_options(self):
        self.driver.find_element(*self.need_help_with_select_filter_options).click()
        self.driver.find_element(*self.fears_and_phobias_select_option).click()

    def clicking_update_button(self):
        self.driver.find_element(*self.update_filter_button).click()

    def seeing_chosen_option(self):
        return self.driver.find_element(*self.fears_and_phobias_button).is_displayed()

    def is_available_therapist_information_displayed(self):
        wait = WebDriverWait(self.driver, 4)
        element = wait.until(ES.presence_of_element_located(self.available_therapists_information))
        return element.is_displayed()