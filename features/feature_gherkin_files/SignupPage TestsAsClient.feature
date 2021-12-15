Feature: User is able to use Signup page functionalities
  User  is able to create new account

  Background:
    Given User is on a Signup page

  Scenario: User is able to create new account
    Then  User clicks on get started button
    When  User fills in email, phone number, create password, and confirm password input fields properly
    Then  User is able to see Submit Button
