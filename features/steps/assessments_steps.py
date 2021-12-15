from behave import given, when, then

from pages.assessments_page import AssessmentPage


@given("User is on a Assessments Page")
def open_assessments_page(context):
    page = AssessmentPage(context)
    page.open_page()
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")
    page.click_assessments_button()


@when("user clicks on Begin Assessment button on Revised Child Anxiety and Depression Scale - Child field")
def click_begin_assessment(context):
    page = AssessmentPage(context)
    page.click_begin_assessment_button_rcads_child()


@then("opens form and select 5 radio buttons with answer 'Always'")
def fill_in_form(context):
    page = AssessmentPage(context)
    page.click_worry_about_things_radio_button()
    page.click_feel_sad_or_empty_radio_button()
    page.click_nothing_is_fun_anymore_radio_button()
    page.click_have_trouble_sleeping_radio_button()
    page.click_problems_with_appetite_radio_button()


@when("clicks on Send Assessment button")
def click_send_assessment_button(context):
    page = AssessmentPage(context)
    page.click_send_assessment_radio_button()


@then("sees assessment completed snackbar")
def see_confirmation_snackbar(context):
    page = AssessmentPage(context)
    assert page.assessment_completed_snackbar_button_displayed()


@when("clicks book now button")
def click_book_now_button(context):
    page = AssessmentPage(context)
    page.click_book_now_button()


@then("is able to see book an appointment page")
def see_book_appointment_page(context):
    page = AssessmentPage(context)
    assert page.book_an_appointment_page_displayed()
