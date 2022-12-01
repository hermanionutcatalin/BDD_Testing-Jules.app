

Feature: Test if we can simulate multiple sign-up
  with multiple users

  Scenario:
    Given I am on the sign-up page of Jules.app
    When I am selecting personal account
    And I am introducing the me yog jatopel309@covbase.com Unique123!
    Then I should be able to reconfirm Unique123! and capture a print screen with the account not-validate message

  Scenario Outline:
    Given I am on the sign-up page of Jules.app
    When I am selecting personal account
    And I am introducing the "<first_name>" "<last_name>" "<email_address>" "<pwd>"
    Then I should be able to reconfirm "<pwd>" and capture a print screen with the account not-validate message
    Examples:
      | first_name | last_name | email_address | pwd |
      | ferof | saxu | ferof53746@cosaxu.com | SuperPass123! |








