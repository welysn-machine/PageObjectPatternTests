
Feature: User is able to use My Account page functionalities
  User is able to change values in input fields in Edit Profile bookmark

  Background:
    Given User is on a My Account Page

  Scenario: User is able to change values in input fields in Edit Profile bookmark
    When User fills in input fields in a form
    Then User clicks save changes button
    #Then User is able to see his records