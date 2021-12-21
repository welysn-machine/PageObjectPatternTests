from behave import given, then, when
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


@given("User is on Login Page")
def open_login_page(context):
    page = LoginPage(context)
    page.open_page()


@when("User fills in password and email input fields with valid credentials")
def log_in_account(context):
    page = LoginPage(context)
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")


@then("User logs in to his account")
def see_main_page(context):
    page = LoginPage(context)
    wait = WebDriverWait(context.driver, 8)
    element = wait.until(ES.presence_of_element_located(page.welcome_tag))
    assert element


@when("User fills in password input field with invalid password")
def fills_in_invalid_password(context):
    page = LoginPage(context)
    page.log_in("jonathan+client@lysnhealth.com.au", "123ly")


@then("User see error message")
def see_error_message(context):
    page = LoginPage(context)
    wait = WebDriverWait(context.driver, 4)
    element = wait.until(ES.presence_of_element_located(page.fail_login_message))
    assert element
