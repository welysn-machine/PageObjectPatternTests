from behave import given, when, then
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from pages.my_consultations_page import MyConsultationsPage


@given("User is logged as a client")
def logging_to_account(context):
    page = MyConsultationsPage(context)
    page.open_page()
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")


@when("User clicks on My Consultations button")
def clicking_my_consultations_button(context):
    page = MyConsultationsPage(context)
    page.clicking_my_consultations_button()
    page.close_twillio_popup()


@then("is able to see History of Consultations")
def seeing_history_of_consultations(context):
    page = MyConsultationsPage(context)
    assert page.is_history_of_sessions_displayed()


@given("User is on a My Consultation Page")
def opening_my_consultations_page(context):
    page = MyConsultationsPage(context)
    page.clicking_my_consultations_button()


@when("clicks on a first position on a list in history")
def clicking_on_first_position_in_history(context):
    page = MyConsultationsPage(context)
    page.clicking_on_first_position_in_history()


@then("is able to see Consultation Details Page")
def seeing_consultation_details_page(context):
    page = MyConsultationsPage(context)
    assert page.is_consultation_details_page_displayed()


@given("User is on a Consultation Details Page")
def opening_consultation_details_page(context):
    page = MyConsultationsPage(context)
    page.clicking_my_consultations_button()
    page.clicking_on_first_position_in_history()


@then("clicks on new message button")
def clicking_new_message_button(context):
    page = MyConsultationsPage(context)

    page.clicking_new_message_button()


@then("types in a information to a psychologist")
def typing_a_message(context):
    page = MyConsultationsPage(context)

    page.typing_a_message("Hello")


@then("clicks Send button and see confirmation popup")
def sending_message_and_see_confirmation_popup(context):
    page = MyConsultationsPage(context)
    page.clicking_send_button()
    wait = WebDriverWait(context.driver, 3)
    element = wait.until(ES.presence_of_element_located(page.confirmation_popup))
    assert element

