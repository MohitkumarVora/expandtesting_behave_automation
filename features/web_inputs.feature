@inputs
Feature: Input Page Automation

    
    Scenario: Verify that valid input values are correctly displayed in the output section
        Given I am on the Inputs page
        When I enter number "123"
        And I enter text "Automation Testing"
        And I enter password "Secret123"
        And I enter date "10-01-2026"
        And I click on display inputs button
        Then I verify that all the input values are entered correctly in output fields
    
    Scenario: Verify that the number input field rejects non-numeric characters
        Given I am on the Inputs page
        When I enter number "abc"
        And I click on display inputs button
        Then I verify that input number field does not accept invlid input number
    
    
    Scenario: Verify that the Clear Inputs button resets all fields and the output section
        Given I am on the Inputs page
        When I enter number "456"
        And I enter text "Cleaning test"
        And I enter password "CleanPass"
        And I enter date "15-05-2026"
        And I click on display inputs button
        And I click on clear inputs button
        Then I verify that all input fields are empty
        And I verify that the output section is hidden