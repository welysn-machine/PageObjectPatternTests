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
    assert page.is_use_tag_displayed()


@then("User logs in to his account")
def see_main_page(context):
    page = MyAccountPage(context)
    page.is_use_tag_displayed()


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
