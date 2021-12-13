from behave import given, when, then



from pages.my_consultations_page import MyConsultationsPage


@given("User is logged as a client")
def log_to_account(context):
    page = MyConsultationsPage(context)
    page.open_page()
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")


@when("User clicks on My Consultations button")
def click_my_consultations_button(context):
    page = MyConsultationsPage(context)
    page.clicking_my_consultations_button()
    page.close_twillio_popup()


@then("is able to see History of Consultations")
def see_history_of_consultations(context):
    page = MyConsultationsPage(context)
    assert page.is_history_of_sessions_displayed()


@given("User is on a My Consultation Page")
def open_my_consultations_page(context):
    page = MyConsultationsPage(context)
    page.clicking_my_consultations_button()


@when("clicks on a first position on a list in history")
def click_on_first_position_in_history(context):
    page = MyConsultationsPage(context)
    page.clicking_on_first_position_in_history()


@then("is able to see Consultation Details Page")
def see_consultation_details_page(context):
    page = MyConsultationsPage(context)
    assert page.is_consultation_details_page_displayed()


@given("User is on a Consultation Details Page")
def open_consultation_details_page(context):
    page = MyConsultationsPage(context)
    page.clicking_my_consultations_button()
    page.clicking_on_first_position_in_history()


@then("clicks on new message button")
def click_new_message_button(context):
    page = MyConsultationsPage(context)

    page.clicking_new_message_button()


@then("types in a information to a psychologist")
def type_a_message(context):
    page = MyConsultationsPage(context)

    page.typing_a_message("Hello")


@then("clicks Send button and see confirmation popup")
def send_message_and_see_confirmation_popup(context):
    page = MyConsultationsPage(context)
    page.clicking_send_button()
    assert page.is_confirmation_popup_displayed()

