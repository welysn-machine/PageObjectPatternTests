from behave import given, when, then

from pages.messages_page import MessagesPage


@given('User is on Messages Page')
def open_messages(context):
    page = MessagesPage(context)
    page.open_page()
    page.log_in("jonathan+client@lysnhealth.com.au", "123lysn123")
    page.click_messages_button()


@then('User is able to see taken message in Inbox')
def check_taken_message_displayed(context):
    page = MessagesPage(context)
    assert page.taken_message_displayed()


@then('User deletes message from Inbox')
def delete_message_inbox_(context):
    page = MessagesPage(context)
    page.delete_message_inbox()


@then('User clicks trash button')
def click_trash_button(context):
    page = MessagesPage(context)
    page.click_trash_button()


@then('User is able to see deleted message in trash')
def check_message_trash_displayed(context):
    page = MessagesPage(context)
    assert page.message_trash_displayed()


@then('User clicks restore taken message button')
def click_restore_message_button(context):
    page = MessagesPage(context)
    page.click_restore_inbox_message_trash()


@then('User clicks restore sent messages button')
def click_restore_message_button(context):
    page = MessagesPage(context)
    page.click_restore_sent_message_trash()


@when('User clicks compose message button')
def click_compose_button(context):
    page = MessagesPage(context)
    page.click_compose_message_button()


@then('User select recipient, fills in subject field and body field')
def fills_in_required_fields(context):
    page = MessagesPage(context)
    page.select_recipient("Lysn-selenium Psych")
    page.fill_in_subject_field("Problems")
    page.fill_in_body_field("More Problems")


@then('User clicks send button and see Sent Messages Page')
def click_see_confirmation(context):
    page = MessagesPage(context)
    page.click_send_button()
    assert page.sent_messages_page_displayed()


@then('User is able to see his message in Sent Messages')
def see_sent_message(context):
    page = MessagesPage(context)
    page.click_sent_messages_button()
    assert page.sent_message_sent_messages_displayed()


@then('User clicks delete button and is able to see his message in trash')
def click_delete_message(context):
    page = MessagesPage(context)
    page.click_delete_sent_messages()
    page.click_trash_button()
    assert page.sent_message_trash_displayed()
