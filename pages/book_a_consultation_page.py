from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from selenium.webdriver.support import expected_conditions as ES

class BookAConsultationPage:

    def __init__(self, context):
        self.driver = context.driver

        self.book_a_consultation_button_from_left_menu = (By.XPATH, "//span[text()='Book a consultation']")
        self.book_button_list_of_available_therapists = (By.XPATH, "//span[text()='Book now']")
        self.length_of_consultation_input_radio_button = (By.ID, "standard")
        self.available_dates = (By.CSS_SELECTOR, "div[data-date='20211231']")
        self.available_time = (By.CLASS_NAME, "timeslots-picker__cell")
        self.book_button_confirm_booking = (By.XPATH, "//span[text()='BOOK']")
        self.confirmation_page = (
            By.XPATH, "//span[text()='BOOK']")
        self.available_therapists_information = (By.CSS_SELECTOR, "img[alt= 'Profile image']")
        self.filer_option = (By.CLASS_NAME, "therapist-filter-trigger")
        self.why_button_from_filter_menu = (By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div/div[2]/div")
        self.fears_and_phobias_select_option = (By.XPATH, "//div[text()='Fears & Phobias']")
        self.update_filter_button = (By.XPATH, "//button[text()='UPDATE']")
        self.no_matches_therapist_information = (By.XPATH,'//h3[text()= "No matches found. Please change your search criteria."]')
        self.clear_all_button_from_filter_menu = (
            By.CLASS_NAME, "label therapist-filter__clear-all therapist-filter__label")

    def clicking_book_a_consultation_button(self):
        self.driver.find_element(*self.book_a_consultation_button_from_left_menu).click()

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
        self.driver.find_element(*self.filer_option).click()

    def select_filter_options(self):
        self.driver.find_element(*self.why_button_from_filter_menu).click()
        self.driver.find_element(*self.fears_and_phobias_select_option).click()
        self.driver.find_element(*self.update_filter_button).click()

    def seeing_empty_list_therapists(self):
        return self.driver.find_element(*self.no_matches_therapist_information).is_displayed()

