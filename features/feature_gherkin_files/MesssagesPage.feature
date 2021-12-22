Feature: User is able to use Messages functionalities
  User is able to see messages in Inbox, delete it and restore
  User is able to write and send a message
  User is able to see sent message in Sent Messages, delete it and restore
  User is able to send a message to a therapist and get a reply

  Background:
    Given User is on Messages Page


  Scenario:User is able to see messages in Inbox, delete it and restore
    Then User is able to see taken message in Inbox
    Then User deletes message from Inbox
    Then User clicks trash button
    Then User is able to see deleted message in trash
    Then User clicks restore taken message button
    Then User is able to see taken message in Inbox

  Scenario:User is able to write and send a message
    When User clicks compose message button
    Then User select recipient, fills in subject field and body field
    Then User clicks send button and see Sent Messages Page


  Scenario:User is able to see sent message in Sent Messages delete it and restore
    Then User is able to see his message in Sent Messages
    Then User clicks delete button and is able to see his message in trash
    Then User clicks restore sent messages button
    Then User is able to see his message in sent messages

  Scenario: User is able to send a message to a therapist and get a reply
    When User is on Compose Message page
    Then User select recipient, fills in subject field, body field and click send button
    Then Therapist sends answer
    Then User is able to see answer in inbox
