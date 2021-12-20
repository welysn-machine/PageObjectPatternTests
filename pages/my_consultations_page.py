from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


class MyConsultationsPage(LoginPage):

    def __init__(self, context):
        super().__init__(context)

        self.driver = context.driver
        self.history_of_sessions = (By.XPATH, "//h6[text()='History']")
        self.first_position_in_history = (By.XPATH, "//p[text()='Psychologist session']")
        self.consultation_details_page = (By.XPATH, "//h6[text()='Consultation Details']")
        self.new_message_button = (By.CSS_SELECTOR, 'div[data-testid*="new-message"]')
        self.text_message_area = (By.CSS_SELECTOR, 'textarea[name*="body"]')
        self.send_button = (By.CSS_SELECTOR, "button[type*='submit']")
        self.confirmation_popup = (By.XPATH, "//div[text()= 'Message sent.']")

    def history_sessions_displayed(self):
        return self.driver.find_element(*self.history_of_sessions).is_displayed()

    def click_first_position_history(self):
        self.driver.find_element(*self.first_position_in_history).click()

    def consultation_details_page_displayed(self):
        return self.driver.find_element(*self.consultation_details_page).is_displayed()

    def click_new_message_button(self):
        self.driver.find_element(*self.new_message_button).click()

    def type_message(self, message):
        self.driver.find_element(*self.text_message_area).send_keys(message)

    def click_send_button(self):
        self.driver.find_element(*self.send_button).click()

    def confirmation_popup_displayed(self):
        wait = WebDriverWait(self.driver, 8)
        element = wait.until(ES.presence_of_element_located(self.confirmation_popup))
        return element.is_displayed()
