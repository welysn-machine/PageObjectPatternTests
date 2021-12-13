from behave import given, when, then



from pages.book_a_consultation_page import BookConsultationPage


@given("User is logged in to his account")
def log_to_account(context):
    page = BookConsultationPage(context)
    page.open_page()
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")


@given("User is on a Book A Consultation Page")
def click_book_a_consultation_button(context):
    page = BookConsultationPage(context)
    page.clicking_book_a_consultation_button()


@when("User choose available Therapist from list using book button")
def choose_available_therapist(context):
    page = BookConsultationPage(context)
    page.close_twillio_popup()
    page.clicking_book_button_available_therapist()


@when("User choose payment type, consultation type, length of consultation")
def choose_payment_consultation_length_and_type(context):
    page = BookConsultationPage(context)
    page.choosing_payment_consultation_type_and_length()


@when("User choose Date and Time of consultation")
def choose_date_and_time(context):
    page = BookConsultationPage(context)
    page.setting_date_and_time()


@then("User is able to book a consultation using book button and sees confirmation page")
def book_a_consultation(context):
    page = BookConsultationPage(context)
    page.booking_a_consultation()
    assert page.confirming_consultation_is_displayed()


@when("User is able to see list with available therapists")
def verify_list_with_therapists(context):
    page = BookConsultationPage(context)
    assert page.is_available_therapist_information_displayed()


@when("Clicks on filter menu")
def click_filter_option(context):
    page = BookConsultationPage(context)
    page.clicking_filter_button()


@when("User choose Fears & Phobias in Select dropdown 'Need help with'")
def set_filter_parameters(context):
    page = BookConsultationPage(context)
    page.select_filter_options()


@when("User clicks Update button")
def vefify_empty_list_of_therapists(context):
    page = BookConsultationPage(context)
    page.clicking_update_button()


@then("User is going back to Book a Consultation Page and is able to see selected Fears & Phobias")
def see_chosen_Fears_and_Phobias_option(context):
    page = BookConsultationPage(context)
    assert page.seeing_chosen_option()
