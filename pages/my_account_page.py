from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.login_page import LoginPage


class MyAccountPage(LoginPage):

    def __init__(self):
        self.edit_profile_button = (By.CSS_SELECTOR, 'div[data-testid="/clients/profile"]')
        self.payments_button = (By.CSS_SELECTOR, 'div[data-testid="/clients/payments"]')
        self.notifications_button = (By.CSS_SELECTOR, 'div[data-testid"/users/notifications"]')
        self.coupons_button = (By.CSS_SELECTOR, 'div[data-testid="/clients/coupons"]')
        self.first_name_input_account = (By.ID, 'user.first_name')
        self.occupation_input_account = (By.ID, 'id-occupation')
        self.date_birth_input_account = (By.CSS_SELECTOR, 'input[placeholder="DD/MM/YYYY"]')
        self.select_marital_input_account = (By.ID, 'id-marital_status')
        self.address_input_account = (By.ID, 'id-user.address')
        self.city_input_account = (By.ID, 'id-user.city')
        self.medicare_number_input_account = (By.ID, 'id-medicare_number')
        # TODO I would like to introduce hier possibility of choice other values on steps level
        self.aboriginal_or_torres_input_account = (By.XPATH, '//span[text()="No"]')
        self.next_of_kin_mobile_number_input_account = (By.ID, 'iid-next_of_kin_phone')
        self.general_practitioner_input_account = (By.ID, 'id-general_practitioner_name')
        self.last_name_input_account = (By.ID, 'id-user.last_name')
        self.place_birth_input_account = (By.ID, 'id-user.gender')
        self.select_gender_input_account = (By.ID, 'place_of_birth')
        self.select_state_input_account = (By.ID, 'id-user.state')
        self.postcode_input_account = (By.ID, 'id-user.postcode')
        self.medicare_reference_input_account = (By.ID, 'id-medicare_reference_number')
        self.next_of_kin_name_input_account = (By.ID, 'id-next_of_kin_name')
        self.next_of_kin_relationship_input_account = (By.ID, 'id-next_of_kin_relationship')
        self.mobile_number_input_account = (By.ID, 'id-user.phone')
        self.general_practitioner_input_account = (By.ID, "id-next_of_kin_relationship")
        self.save_changes_account_button = (By.XPATH, '//span[text()="SAVE CHANGES"]')

    def click_edit_profile_button(self):
        self.driver.find_element(*self.edit_profile_button).click()

    def click_save_changes_button(self):
        self.driver.find_element(*self.save_changes_account_button).click()

    def type_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input_account).clear().send_keys(first_name)

    def type_occupation(self, occupation):
        self.driver.find_element(*self.first_name_input_account).clear().send_keys(occupation)

    def type_date_birth(self, date):
        self.driver.find_element(*self.first_name_input_account).clear().send_keys(date)

    def select_marital(self, marital):
        select = Select(self.driver.find_element(*self.select_marital_input_account))
        select.select_by_visible_text(marital)

    def type_address(self, address):
        self.driver.find_element(*self.address_input_account).clear().send_keys(address)

    def type_city(self, city):
        self.driver.find_element(*self.city_input_account).clear().send_keys(city)

    def type_medicare_number(self, medicare_numer):
        self.driver.find_element(*self.first_name_input_account).clear().send_keys(medicare_numer)

    def choose_aboriginal_or_torres(self):
        self.driver.find_element(*self.aboriginal_or_torres_input_account).click()

    def type_next_of_kin_number(self, mobile_number):
        self.driver.find_element(*self.first_name_input_account).clear().send_keys(mobile_number)






