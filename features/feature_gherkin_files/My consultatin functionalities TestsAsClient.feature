
Feature: User is able to use My Consulations functionalities
  User is able to see history of his sessions
  User is able to see Consultation Details page and an invoice after a session
  User is able to send new message and attach a file to a therapist


  Scenario: User is able to see history of his sessions
    Given User is logged in as a client
    When User clicks on My Consultations button
    Then is able to see History of Consultations

  Scenario: User is able to see Consultation Details page and an invoice after a session
      Given User is on a History of Consultations Page

  Scenario: User is able to send new message and attach a file to a therapist
