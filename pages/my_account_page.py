from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from pages.login_page import LoginPage


class MyAccountPage(LoginPage):

    def __init__(self, context):
        self.driver = context.driver
        super().__init__(context)

        self.edit_profile_button = (By.CSS_SELECTOR, 'div[data-testid="/clients/profile"]')
        self.payments_button = (By.CSS_SELECTOR, 'div[data-testid="/clients/payments"]')
        self.notifications_button = (By.CSS_SELECTOR, 'div[data-testid"/users/notifications"]')
        self.coupons_button = (By.CSS_SELECTOR, 'div[data-testid="/clients/coupons"]')
        self.email_input_my_account_page = (By.ID, 'id-user.email')
        self.first_name_input_account = (By.ID, 'id-user.first_name')
        self.occupation_input_account = (By.ID, 'id-occupation')
        self.date_birth_input_account = (By.CSS_SELECTOR, 'input[placeholder="DD/MM/YYYY"]')
        self.select_marital_input_account = (By.ID, 'id-marital_status')
        self.address_input_account = (By.ID, 'id-user.address')
        self.city_input_account = (By.ID, 'id-user.city')
        self.medicare_number_input_account = (By.ID, 'id-medicare_number')
        # TODO I would like to introduce hier possibility of choice other values on steps level
        self.aboriginal_or_torres_input_account = (By.XPATH, '//span[text()="No"]')
        self.aboriginal_or_torres_input_account_value_no = (By.CSS_SELECTOR, 'input[value="no"]')
        self.next_of_kin_mobile_number_input_account = (By.ID, 'id-next_of_kin_phone')
        self.general_practitioner_name_input_account = (By.ID, 'id-general_practitioner_name')
        self.last_name_input_account = (By.ID, 'id-user.last_name')
        self.place_birth_input_account = (By.ID, 'id-user.gender')
        self.select_gender_input_account = (By.ID, 'id-user.gender')
        self.select_state_input_account = (By.ID, 'id-user.state')
        self.postcode_input_account = (By.ID, 'id-user.postcode')
        self.medicare_reference_input_account = (By.ID, 'id-medicare_reference_number')
        self.next_of_kin_name_input_account = (By.ID, 'id-next_of_kin_name')
        self.select_next_of_kin_relationship_input_account = (By.ID, 'id-next_of_kin_relationship')
        self.mobile_number_input_account = (By.ID, 'id-user.phone')
        self.general_practitioner_phone_input_account = (By.ID, "id-next_of_kin_relationship")
        self.save_changes_account_button = (By.XPATH, '//span[text()="SAVE CHANGES"]')

    def type_email(self, email):
        email_field = self.driver.find_element(*self.email_input_my_account_page)
        email_field.click()
        email_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        email_field.send_keys(email)

    def click_edit_profile_button(self):
        self.driver.find_element(*self.edit_profile_button).click()

    def click_save_changes_button(self):
        self.driver.find_element(*self.save_changes_account_button).click()

    def type_first_name(self, first_name):
        first_name_field = self.driver.find_element(*self.first_name_input_account)
        first_name_field.click()
        first_name_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        first_name_field.send_keys(first_name)

    def type_occupation(self, occupation):
        occupation_field = self.driver.find_element(*self.occupation_input_account)
        occupation_field.click()
        occupation_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        occupation_field.send_keys(occupation)

    def type_date_birth(self, date):
        date_birth_field = self.driver.find_element(*self.date_birth_input_account)
        date_birth_field.click()
        date_birth_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        date_birth_field.send_keys(date)

    def select_marital(self, marital):
        select = Select(self.driver.find_element(*self.select_marital_input_account))
        select.select_by_visible_text(marital)

    def type_address(self, address):
        address_field = self.driver.find_element(*self.address_input_account)
        address_field.click()
        address_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        address_field.send_keys(address)

    def type_city(self, city):
        city_field = self.driver.find_element(*self.city_input_account)
        city_field.click()
        city_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        city_field.send_keys(city)

    def type_medicare_number(self, medicare_numer):
        medicare_number_field = self.driver.find_element(*self.medicare_number_input_account)
        medicare_number_field.click()
        medicare_number_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        medicare_number_field.send_keys(medicare_numer)

    def choose_aboriginal_or_torres(self):
        self.driver.find_element(*self.aboriginal_or_torres_input_account).click()

    def type_next_of_kin_number(self, mobile_number):
        next_kin_number = self.driver.find_element(*self.next_of_kin_mobile_number_input_account)
        next_kin_number.click()
        next_kin_number.send_keys(Keys.BACKSPACE * 9)
        next_kin_number.send_keys(mobile_number)

    def type_general_practitioner_number(self, practitioner_number):
        practitioner_number_field = self.driver.find_element(*self.general_practitioner_name_input_account)
        practitioner_number_field.click()
        practitioner_number_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        practitioner_number_field.send_keys(practitioner_number)

    def type_last_name(self, last_name):
        last_name_field = self.driver.find_element(*self.last_name_input_account)
        last_name_field.click()
        last_name_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        last_name_field.send_keys(last_name)

    def type_mobile_number(self, mobile_number):
        mobile_number_field = self.driver.find_element(*self.mobile_number_input_account)
        mobile_number_field.click()
        mobile_number_field.send_keys(Keys.BACKSPACE * 9)
        mobile_number_field.send_keys(mobile_number)

    def select_gender(self, gender):
        select = Select(self.driver.find_element(*self.select_gender_input_account))
        select.select_by_visible_text(gender)

    def type_place_of_birth(self, place_birth):
        place_birth_field = self.driver.find_element(*self.place_birth_input_account)
        place_birth_field.click()
        place_birth_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        place_birth_field.send_keys(place_birth)

    def select_state(self, state):
        select = Select(self.driver.find_element(*self.select_state_input_account))
        select.select_by_visible_text(state)

    def type_postcode(self, postcode):
        postcode_field = self.driver.find_element(*self.postcode_input_account)
        postcode_field.click()
        postcode_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        postcode_field.send_keys(postcode)

    def type_medicare_reference_number(self, reference_number):
        reference_number_field = self.driver.find_element(*self.medicare_reference_input_account)
        reference_number_field.click()
        reference_number_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        reference_number_field.send_keys(reference_number)

    def type_next_of_kin_name(self, kin_name):
        next_kin_name = self.driver.find_element(*self.next_of_kin_name_input_account)
        next_kin_name.click()
        next_kin_name.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        next_kin_name.send_keys(kin_name)

    def select_kin_relationship(self, relationship):
        select = Select(self.driver.find_element(*self.select_next_of_kin_relationship_input_account))
        select.select_by_visible_text(relationship)

    def type_general_practitioner_phone(self, phone):
        practitioner_phone_field = self.driver.find_element(*self.general_practitioner_phone_input_account)
        practitioner_phone_field.click()
        practitioner_phone_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        practitioner_phone_field.send_keys(phone)

    def email_get_attribute(self, text):
        email_text = self.driver.find_element(*self.email_input_my_account_page).get_attribute("value")
        assert email_text == text

    def first_name_get_attribute(self, text):
        first_name_text = self.driver.find_element(*self.first_name_input_account).get_attribute("value")
        assert first_name_text == text

    def occupation_get_attribute(self, text):
        occupation_text = self.driver.find_element(*self.occupation_input_account).get_attribute("value")
        assert occupation_text == text

    def date_birth_get_attribute(self, text):
        date_birth_text = self.driver.find_element(*self.date_birth_input_account).get_attribute("value")
        assert date_birth_text == text

    def select_marital_get_attribute(self, text):
        select_marital_text = self.driver.find_element(*self.select_marital_input_account).get_attribute("value")
        assert select_marital_text == text

    def address_get_attribute(self, text):
        address_text = self.driver.find_element(*self.address_input_account).get_attribute("value")
        assert address_text == text

    def city_get_attribute(self, text):
        city_text = self.driver.find_element(*self.city_input_account).get_attribute("value")
        assert city_text == text

    def medicare_number_get_attribute(self, text):
        medicare_number = self.driver.find_element(*self.medicare_number_input_account).get_attribute("value")
        assert medicare_number == text

    def aboriginal_or_torres_get_attribute(self, text):
        aboriginal_torres_selected = self.driver.find_element(
            *self.aboriginal_or_torres_input_account_value_no).is_selected()
        assert aboriginal_torres_selected
        aboriginal_torres_text = self.driver.find_element(
            *self.aboriginal_or_torres_input_account_value_no).get_attribute("value")
        assert aboriginal_torres_text == text

    def next_kin_number_get_attribute(self, text):
        next_kin_number_text = self.driver.find_element(*self.next_of_kin_mobile_number_input_account).get_attribute(
            "value")
        assert next_kin_number_text == text

    def last_name_get_attribute(self, text):
        last_name_text = self.driver.find_element(*self.last_name_input_account).get_attribute("value")
        assert last_name_text == text

    def mobile_number_get_attribute(self, text):
        mobile_number_text = self.driver.find_element(*self.mobile_number_input_account).get_attribute("value")
        assert mobile_number_text == text

    def select_gender_get_attribute(self, text):
        gender_text = self.driver.find_element(*self.select_gender_input_account).get_attribute("value")
        assert gender_text == text

    def select_state_get_attribute(self, text):
        state_text = self.driver.find_element(*self.select_state_input_account).get_attribute("value")
        assert state_text == text

    def postcode_get_attribute(self, text):
        postcode_text = self.driver.find_element(*self.postcode_input_account).get_attribute("value")
        assert postcode_text == text

    def medicare_reference_number_get_attribute(self, text):
        medicale_reference_text = self.driver.find_element(*self.medicare_reference_input_account).get_attribute(
            "value")
        assert medicale_reference_text == text

    def next_kin_name_get_attribute(self, text):
        next_kin_name_text = self.driver.find_element(*self.next_of_kin_name_input_account).get_attribute("value")
        assert next_kin_name_text == text

    def select_kin_relationship_get_attribute(self, text):
        kin_relationship_text = self.driver.find_element(
            *self.select_next_of_kin_relationship_input_account).get_attribute("value")
        assert kin_relationship_text == text
