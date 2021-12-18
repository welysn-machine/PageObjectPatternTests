from behave import given, when, then

from pages.book_a_consultation_page import BookConsultationPage


@given("User is logged in to his account")
def log_in_account(context):
    page = BookConsultationPage(context)
    page.open_page()
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")


@given("User is on a Book A Consultation Page")
def click_book_consultation_button(context):
    page = BookConsultationPage(context)
    page.click_book_consultation_button()
    page.click_book_psychologist_button()

@when("User choose available Therapist from list using book button")
def choose_available_therapist(context):
    page = BookConsultationPage(context)
    page.close_twillio_popup()
    page.click_book_button_available_therapist()


@when("User choose payment type, consultation type, length of consultation")
def choose_payment_consultation_length_type(context):
    page = BookConsultationPage(context)
    page.choose_payment_consultation_type_length()


@when("User choose Date and Time of consultation")
def choose_date_time(context):
    page = BookConsultationPage(context)
    page.set_date_time()


@then("User is able to book a consultation using book button and sees confirmation page")
def book_consultation(context):
    page = BookConsultationPage(context)
    page.book_consultation()
    assert page.confirm_consultation_displayed()


@when("User is able to see list with available therapists")
def verify_list_with_therapists(context):
    page = BookConsultationPage(context)
    assert page.available_therapist_information_displayed()


@when("Clicks on filter menu")
def click_filter_option(context):
    page = BookConsultationPage(context)
    page.click_filter_button()


@when("User choose Fears & Phobias in Select dropdown 'Need help with'")
def set_filter_parameters(context):
    page = BookConsultationPage(context)
    page.select_filter_options()


@when("User clicks Update button")
def verify_empty_list_therapists(context):
    page = BookConsultationPage(context)
    page.click_update_button()


@then("User is going back to Book a Consultation Page and is able to see selected Fears & Phobias")
def see_chosen_Fears_Phobias_option(context):
    page = BookConsultationPage(context)
    assert page.see_chosen_option()
