
Feature: User as a client is able to book a consultation
         User is able to use filter options

  Scenario: User is able to book a consultation
    Given User is on a Book A Consultation Page
    When  User choose available Therapist from list using book button
    When  User choose payment type, consultation type, length of consultation
    When  User choose Date and Time of consultation
    Then  User is able to book a consultation using book button and sees confirmation page

  Scenario: User is able to use filter options
    Given User is on a Book A Consultation Page
    When  User is able to see list with available therapists
    When  Clicks on filter menu
    Then  is able to personalize his expectations
    Then  is not able to sees list with available therapists



