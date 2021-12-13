Feature: User is able to use Assessment Page functionalities
  User is able to fulfill Assessment, form send and book a consultation immediately

  Background:

    Given  User is on a Assessments Page

  Scenario: User is able to fulfill Assessment, form send and book a consultation immediately
    When user clicks on Begin Assessment button on Revised Child Anxiety and Depression Scale - Child field
    Then opens form and select 5 radio buttons with answer 'Always'
    When clicks on Send Assessment button
    Then sees assessment completed snackbar
    When clicks book now button
    Then is able to see book an appointment page