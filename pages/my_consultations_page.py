from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


class MyConsultationsPage(LoginPage):

    def __init__(self, context):
        super().__init__(context)

        self.driver = context.driver
        self.history_of_sessions = (By.CSS_SELECTOR, "5982")
        self.first_position_in_history = (By.ID, "5982")
        self.consultation_details_page = (By.XPATH, "//h6[text()='Consultation Details']")
        self.new_message_button = (By.CSS_SELECTOR, 'div[data-testid*="new-message"]')
        self.text_message_area = (By.CSS_SELECTOR, 'textarea[name*="body"]')
        self.send_button = (By.CSS_SELECTOR, "button[type*='submit']")
        self.confirmation_popup = (By.XPATH, "//div[text()= 'Message sent.']")

    def is_history_of_sessions_displayed(self):
        return self.driver.find_element(*self.history_of_sessions).is_displayed()

    def clicking_on_first_position_in_history(self):
        element = self.driver.find_element(By.ID, "5982")
        webdriver.ActionChains(self.driver).move_to_element(element).click(element)

    def is_consultation_details_page_displayed(self):
        return self.driver.find_element(*self.consultation_details_page).is_displayed()

    def clicking_new_message_button(self):
        self.driver.find_element(*self.new_message_button).click()

    def typing_a_message(self, message):
        self.driver.find_element(*self.text_message_area).send_keys(message)

    def clicking_send_button(self):
        self.driver.find_element(*self.send_button).click()

    def is_confirmation_popup_displayed(self):
        return self.driver.find_element(*self.confirmation_popup).is_displayed()
