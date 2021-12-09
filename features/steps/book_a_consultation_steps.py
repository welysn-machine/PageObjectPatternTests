from behave import given, when, then
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from pages.book_a_consultation_page import BookAConsultationPage


@given("User is logged in to his account")
def logging_to_account(context):
    page = BookAConsultationPage(context)
    page.open_page()
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")


@given("User is on a Book A Consultation Page")
def clicking_book_a_consultation_button(context):
    page = BookAConsultationPage(context)
    page.clicking_book_a_consultation_button()


@when("User choose available Therapist from list using book button")
def choosing_available_therapist(context):
    page = BookAConsultationPage(context)
    page.clicking_book_button_available_therapist()


@when("User choose payment type, consultation type, length of consultation")
def choosing_payment_consultation_length_and_type(context):
    page = BookAConsultationPage(context)
    page.choosing_payment_consultation_type_and_length()


@when("User choose Date and Time of consultation")
def choosing_date_and_time(context):
    page = BookAConsultationPage(context)
    page.setting_date_and_time()


@then("User is able to book a consultation using book button and sees confirmation page")
def booking_a_consultation(context):
    page = BookAConsultationPage(context)
    page.booking_a_consultation()
    assert page.confirming_consultation_is_displayed()


@when("User is able to see list with available therapists")
def verifying_list_with_therapists(context):
    page = BookAConsultationPage(context)
    wait = WebDriverWait(context.driver, 4)
    element = wait.until(ES.presence_of_element_located(page.available_therapists_information))
    assert element


@when("Clicks on filter menu")
def clicking_filter_option(context):
    page = BookAConsultationPage(context)
    page.clicking_filter_button()


@when("User choose Fears & Phobias in Select dropdown 'Need help with'")
def setting_filter_parameters(context):
    page = BookAConsultationPage(context)
    page.select_filter_options("Fears & Phobias")


@when("User clicks Update button")
def vefifying_empty_list_of_therapists(context):
    page = BookAConsultationPage(context)
    page.clicking_update_button()


@then("User is going back to Book a Consultation Page and is able to see selected Fears & Phobias")
def seeing_chosen_Fears_and_Phobias_option(context):
    page = BookAConsultationPage(context)
    assert page.seeing_chosen_option()
