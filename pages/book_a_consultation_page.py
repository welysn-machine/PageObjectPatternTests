from selenium.webdriver.common.by import By


class BookAConsultationPage:

    def __init__(self, context):
        self.driver = context.driver

        self.book_button = (By.CSS_SELECTOR, "span[.*='Book now']")
        self.length_of_consultation_input_radio_button = (By.ID, "standard")
        self.available_dates = (By.CLASS_NAME, "day after therapist-calendar__day--available")
        self.available_time = (By.CLASS_NAME,"timeslots-picker__cell")
        self.book_button = (By.CSS_SELECTOR, "span[.*='BOOK']")
        self.confirmation_page = (By.CSS_SELECTOR,"div[.*='Your booking is confirmed, please take a moment to prepare for your session.']")
        self.available_therapists_information = (By.CSS_SELECTOR, "span[.*='2 Psychologists are available in the next month']")
        self.filer_option = (By.CLASS_NAME, "therapist-filter-trigger")

