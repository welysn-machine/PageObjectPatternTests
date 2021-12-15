Feature: User as a client is able to use Login page functionalities
  User is able to log in on his account with valid credentials
  User is not able to log in to his account with invalid password
  User is able to create new account

  Background:
    Given User is on Login Page

  Scenario: User is able to log in to his account
    When  User fills in password and email input fields with valid credentials
    Then  User logs in to his account

  Scenario: User is not able to log in to his account
    When  User fills in password input field with invalid password
    Then  User see error message

