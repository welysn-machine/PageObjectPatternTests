from behave import given, when, then

from pages.signup_page import SignupPage


@given("User is on a Signup page")
def opening_signup_page(context):
    page = SignupPage(context)
    page.open_page()
    page.get_started_button


@then("User clicks on get started button")
def click_get_started_button(context):
    page = SignupPage(context)
    page.click_get_started_button()


@when("User fills in email, phone number, create password, and confirm password input fields properly")
def creating_account(context):
    page = SignupPage(context)
    page.create_account("newclient@gmail.com", "491570159", "newclient12", "newclient12")


@then("User is able to see Submit Button")
def see_submit_buttton(context):
    page = SignupPage(context)
    assert page.verify_phone_number_submit_button_displayed()
