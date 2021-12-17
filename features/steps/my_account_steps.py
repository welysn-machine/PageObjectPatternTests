from behave import given, when, then

from pages.my_account_page import MyAccountPage


@given("User is on a My Account Page")
def open_my_account_page(context):
    page = MyAccountPage(context)
    page.open_page()
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")
    page.click_my_account_button()


@when("User fills in input fields in a form")
def open_my_account_page(context):
    page = MyAccountPage(context)
    page.type_email("jonathan+client@lysnhealth.com.au")
    page.type_first_name("Jonathan")
    page.type_occupation("Techie")
    page.type_date_birth("01/01/1980")
    page.select_marital("Single")
    page.type_address("Brisbane")
    page.type_city("Brisbane")
    page.type_medicare_number("1231231231")
    page.choose_aboriginal_or_torres()
    page.type_next_of_kin_number("491570156")
    page.type_last_name("King")
    page.type_mobile_number("488870273")
    page.select_gender("Male")
    page.select_state("Queensland")
    page.type_postcode("4006")
    page.type_medicare_reference_number("123")
    page.type_next_of_kin_name("1234")
    page.select_kin_relationship("Father")


@then("User clicks save changes button")
def click_save_changes_button(context):
    page = MyAccountPage(context)
    page.click_save_changes_button()


@then("User is able to see his records")
def see_all_records(context):
    page = MyAccountPage(context)
    page.email_get_attribute("jonathan+client@lysnhealth.com.au")
    page.first_name_get_attribute("Jonathan")
    page.occupation_get_attribute("Techie")
    page.date_birth_get_attribute("01/01/1980")
    page.select_marital_get_attribute("single")
    page.address_get_attribute("Brisbane")
    page.city_get_attribute("Brisbane")
    page.medicare_number_get_attribute("1231231231")
    page.aboriginal_or_torres_get_attribute("no")
    page.next_kin_number_get_attribute("+61491570156")
    page.last_name_get_attribute("King")
    page.mobile_number_get_attribute("+61488870273")
    page.select_gender_get_attribute("male")
    page.select_state_get_attribute("QLD")
    page.postcode_get_attribute("4006")
    page.medicare_reference_number_get_attribute("123")
    page.next_kin_name_get_attribute("1234")
    page.select_kin_relationship_get_attribute("Father")
