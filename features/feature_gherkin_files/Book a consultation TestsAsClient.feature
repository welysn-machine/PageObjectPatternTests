Feature: User as a client is able to book a consultation
  User is able to use filter options

  Background:
    Given User is logged in to his account
    Given User is on a Book A Consultation Page

  Scenario: User is able to book a consultation
    When  User choose available Therapist from list using book button
    When  User choose payment type, consultation type, length of consultation
    When  User choose Date and Time of consultation
    Then  User is able to book a consultation using book button and sees confirmation page

  Scenario: User is able to use filter options
    When  Clicks on filter menu
    When  User choose Fears & Phobias in Select dropdown 'Need help with'
    When  User clicks Update button
    Then  User is going back to Book a Consultation Page and is able to see selected Fears & Phobias



