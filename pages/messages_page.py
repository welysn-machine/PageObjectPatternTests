from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


class MessagesPage(LoginPage):

    def __init__(self,context):
        self.driver = context.driver
        super().__init__(context)

        self.taken_message = (By.CSS_SELECTOR, "td[value*='25/11/2021 10:39am'] " )
        self.delete_button_inbox = (By.CSS_SELECTOR, "span[data-testid='delete-message-icon']")
        self.trash_button = (By.CSS_SELECTOR, "div[data-testid='trash']")
        self.message_trash = (By.CSS_SELECTOR, 'td[value="25/11/2021 10:39am"]')
        self.restore_sent_message_trash = (By.XPATH, '//tbody/tr[1]/td[4]/div/button')
        self.restore_inbox_message_trash = (By.XPATH, '//tbody/tr[1]/td[4]/div/button')
        self.compose_message_button = (By.CSS_SELECTOR, 'button[data-testid="add-message-fab"]')
        self.select_recipient_dropdown = (By.CSS_SELECTOR,'select[id="id-recipient"]' )
        self.send_button = (By.XPATH, '//button/span[text()="Send"]')
        self.subject_input_field = (By.CSS_SELECTOR, 'input[id="id-subject"]')
        self.body_input_field = (By.CSS_SELECTOR,'textarea[name="body"]')
        self.confirmation_sent_message = (By.XPATH, "//div[text()='Message sent']")
        self.sent_message_in_sent_messages = (By.CSS_SELECTOR, "tr[index='0']>td[value='Problems']")
        self.delete_button_sent_messages = (By.CSS_SELECTOR, "span[data-testid='delete-message-icon']")
        self.sent_message_trash = (By.CSS_SELECTOR, "tr[index='0']>td[value='Problems']")
        self.sent_messages_button  = (By.CSS_SELECTOR, "div[data-testid='sent']")

    def taken_message_displayed(self):
        return self.driver.find_element(*self.taken_message).is_displayed()

    def delete_message_inbox(self):
        self.driver.find_element(*self.delete_button_inbox).click()

    def click_trash_button(self):
        self.driver.find_element(*self.trash_button).click()

    def message_trash_displayed(self):
        wait = WebDriverWait(self.driver,4)
        element = wait.until(ES.presence_of_element_located(self.message_trash))
        return element.is_displayed()

    def click_restore_inbox_message_trash(self):
        self.driver.find_element(*self.restore_inbox_message_trash).click()

    def click_restore_sent_message_trash(self):
        self.driver.find_element(*self.restore_sent_message_trash).click()

    def click_compose_message_button(self):
        self.driver.find_element(*self.compose_message_button).click()

    def fill_in_subject_field(self,message_subject):
        self.driver.find_element(*self.subject_input_field).send_keys(message_subject)


    def fill_in_body_field(self,message_body):
        self.driver.find_element(*self.body_input_field).send_keys(message_body)

    def click_send_button(self):
        self.driver.find_element(*self.send_button).click()

    def select_recipient(self,recipient):
        select = Select(self.driver.find_element(*self.select_recipient_dropdown))
        select.select_by_visible_text(recipient)

    def message_sent_displayed(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(ES.presence_of_element_located(self.confirmation_sent_message))
        return element.is_displayed()

    def sent_message_sent_messages_displayed(self):
        self.driver.find_element(*self.sent_message_in_sent_messages).is_displayed()

    def click_delete_sent_messages(self):
        self.driver.find_element(*self.delete_button_sent_messages).click()

    def sent_message_trash_displayed(self):
        self.driver.find_element(*self.sent_message_trash).is_displayed()

    def click_sent_messages_button(self):
        self.driver.find_element(*self.sent_messages_button).click()

