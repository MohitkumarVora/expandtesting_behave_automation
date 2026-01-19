from behave import given, when, then
from features.pages.web_input_page import WebInputPage
from datetime import datetime

@given('I am on the Inputs page')
def step_open_web_input_page(context):
    context.web_input = WebInputPage(context.driver)
    context.web_input.open()

@when('I enter number "{inputnumber}"')
def step_enter_number(context, inputnumber):
    context.entered_number = inputnumber
    context.web_input.enter_number(inputnumber)
    print(inputnumber)


@when('I enter text "{inputtext}"')
def step_enter_text(context, inputtext):
    context.entered_text = inputtext
    context.web_input.enter_text(inputtext)
    print(inputtext)


@when('I enter password "{inputpassword}"')
def step_enter_password(context, inputpassword):
    context.entered_password = inputpassword
    context.web_input.enter_password(inputpassword)
    print(inputpassword)


@when('I enter date "{inputdate}"')
def step_enter_date(context, inputdate):
    
    context.entered_date = inputdate
    context.web_input.enter_date(inputdate)
    print(inputdate)


@when('I click on display inputs button')
def step_click_display_inputs(context):
    context.web_input.click_display_inputs()


@when('I click on clear inputs button')
def step_click_clear_inputs(context):
    context.web_input.click_clear_inputs()


@then('I verify that all the input values are entered correctly in output fields')
def step_verify_valid_inputs(context):
    actual_number = context.web_input.get_input_number()
    actual_text = context.web_input.get_input_text()
    actual_password = context.web_input.get_input_password()
    
    # This is the string from the website (e.g., "2026-01-10")
    actual_date_str = context.web_input.get_input_date() 

    # 1. Convert the date you entered (DD-MM-YYYY) into a date object
    # Use '%d-%m-%Y' to match your input format
    expected_date_obj = datetime.strptime(context.entered_date, '%d-%m-%Y').date()

    # 2. Convert the date from the output field (YYYY-MM-DD) into a date object
    actual_date_obj = datetime.strptime(actual_date_str, '%Y-%m-%d').date()

    # Standard assertions
    assert actual_number == context.entered_number, f"Expected Number '{context.entered_number}', but got '{actual_number}'"
    assert actual_text == context.entered_text, f"Expected Text '{context.entered_text}', but got '{actual_text}'"
    assert actual_password == context.entered_password, f"Expected Text '{context.entered_password}', but got '{actual_password}'"
    
    # 3. Compare the objects, not the strings
    assert actual_date_obj == expected_date_obj, f"Expected Date '{expected_date_obj}', but got '{actual_date_obj}'"


@then('I verify that input number field does not accept invlid input number')
def step_verify_invalid_input(context):
    actual_number = context.web_input.get_input_number()
    assert actual_number == "", (f"Expected Number '{context.entered_number}', but got '{actual_number}'")


@then('I verify that all input fields are empty')
def step_verify_fields_cleared(context):
    # We check if the 'value' attribute is an empty string
    assert context.web_input.get_number_value() == "", "Number field was not cleared"
    assert context.web_input.get_text_value() == "", "Text field was not cleared"
    assert context.web_input.get_password_value() == "", "Password field was not cleared"
    assert context.web_input.get_date_value() == "", "Date field was not cleared"

@then('I verify that the output section is hidden')
def step_verify_output_hidden(context):
    # On this site, 'clearing' resets the output text to an empty string
    actual_num = context.web_input.get_input_number()
    actual_text = context.web_input.get_input_text()
    
    assert actual_num == "", f"Output number should be empty, but got '{actual_num}'"
    assert actual_text == "", f"Output text should be empty, but got '{actual_text}'"