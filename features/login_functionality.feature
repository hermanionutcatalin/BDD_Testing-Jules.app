Feature: Testing Jules app with BDD
  as a user
  I want to test the Login Functionality
  when putting different credentials on the Login Page of Jules.app

  Scenario: testing invalid credentials login
    Given I am on website Jules.app login page
    When I enter an invalid user name
    And I enter an invalid password
    Then I am not able to press the login button
    And Close the browser

  Scenario: testing valid credentials but no validated user login
    Given I am on website Jules.app login page
    When I enter a valid user name
    And I enter a valid password
    And I press submit button
    Then I receive the non validated user message
    And Close the browser


  Scenario: testing not validated with correct email user but invalid pass
    Given I am on website Jules.app login page
    When I enter a non validated user name
    And I enter an invalid password
    And I press submit button
    Then I receive the Incorrect email/pass message
    And Close the browser

  Scenario: testing if blank user name message appear
    Given I am on website Jules.app login page
    When I enter an invalid user name
    Then I see the enter a valid user message
    And Close the browser

  Scenario: testing if blank password message appear
    Given I am on website Jules.app login page
    When I enter a valid user name
    And I enter a password then delete it
    Then I see the enter a valid pass message
    And Close the browser