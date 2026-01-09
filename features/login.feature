Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter the username "practice"
    And I enter the password "SuperSecretPassword!"
    And I click on the Login Button
    Then I verify that the user is redirect to "/secure" page.
    And I confirm the success message "You logged into a secure area!" is visible
    And I verify that a Logout button is displayed
  
  Scenario: Verify login with Invalid username
    Given I am on the login page
    When I enter the username "testinguser"
    And I enter the password "SuperSecretPassword!"
    And I click on the Login Button
    Then I verify that a username error message "Your username is invalid!" is displayed
    And I confirm to remain on login page

  Scenario: Verify login with Invalid password
    Given I am on the login page
    When I enter the username "practice"
    And I enter the password "WrongPassword"
    And I click on the Login Button
    Then I verify that a password error message "Your password is invalid!" is displayed
    And I confirm to remain on login page
    
    Scenario: Verify login with Invalid username and password
    Given I am on the login page
    When I enter the username "testinguser"
    And I enter the password "WrongPassword"
    And I click on the Login Button
    Then I verify that a password error message "Your username is invalid!" is displayed
    And I confirm to remain on login page