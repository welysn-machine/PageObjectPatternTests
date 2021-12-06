from behave import given, when, then
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from pages.my_account_page import MyAccountPage


@given("User is on Login Page")
def open_login_page(context):
    page = MyAccountPage(context)
    page.open_page()


@when("User fills in password and email input fields with valid credentials")
def fills_in_valid_credentials(context):
    page = MyAccountPage(context)
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")
    assert page.is_welcome_tag_displayed()


@then("User logs in to his account")
def see_main_page(context):
    page = MyAccountPage(context)
    page.is_welcome_tag_displayed()


@when("User fills in password input field with invalid password")
def fills_in_invalid_password(context):
    page = MyAccountPage(context)
    page.log_in("jonathan+client@lysnhealth.com.au", "123ly")


@then("User see error message")
def see_error_message(context):
    page = MyAccountPage(context)
    wait = WebDriverWait(context.driver, 4)
    element = wait.until(ES.presence_of_element_located(page.fail_login_message))
    assert element


@then("User clicks on get started button")
def click_get_started_button(context):
    page = MyAccountPage(context)
    page.click_get_started_button()


@when("User fills in email, phone number, create password, and confirm password input fields properly")
def creating_account(context):
    page = MyAccountPage(context)
    page.create_account("newclient@gmail.com", "491570159", "newclient12", "newclient12")


@then("User is able to see Submit Button")
def see_submit_buttton(context):
    page = MyAccountPage(context)
    assert page.verify_phone_number_submit_button_displayed()
