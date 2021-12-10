
Feature: User is able to use My Consulations functionalities
  User is able to see history of his sessions
  User is able to see Consultation Details Page with paid invoices
  User is able to send new message to a therapist
  Background:
    Given User is logged as a client


  Scenario: User is able to see history of his sessions
    When User clicks on My Consultations button
    Then is able to see History of Consultations

  Scenario: User is able to see Consultation Details with paid invoices
      Given User is on a My Consultation Page
      When  clicks on a first position on a list in history
      Then  is able to see Consultation Details Page

  Scenario: User is able to send new message to a therapist
      Given  User is on a Consultation Details Page
      Then   clicks on new message button
      Then   types in a information to a psychologist
      Then   clicks Send button and see confirmation popup