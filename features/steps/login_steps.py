from behave import given, when, then
from features.pages.login_page import LoginPage


@given("I am on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I enter the username "{username}"')
def step_enter_username(context, username):
    context.login_page.enter_username(username)
    print(username)


@when('I enter the password "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password)
    print(password)


@when("I click on the Login Button")
def step_click_login(context):
    context.login_page.click_login()


@then('I verify that the user is redirect to "{expected_url}" page.')
def step_verify_redirect(context, expected_url):
    context.login_page.wait_for_url_contains(expected_url)
    assert expected_url in context.driver.current_url


@then('I confirm the success message "{expected_message}" is visible')
def step_verify_success_message(context, expected_message):
    context.login_page.wait_for_url_contains("/secure")
    actual_message = context.login_page.get_success_message()
    assert expected_message in actual_message



@then("I verify that a Logout button is displayed")
def step_verify_logout_button(context):
    assert context.login_page.is_logout_button_displayed(), (
        "Logout button is not displayed"
    )


@then('I verify that a username error message "{expected_error}" is displayed')
def step_verify_username_error_message(context, expected_error):
    actual_error = context.login_page.get_error_message()
    print(expected_error,"------" , actual_error)
    assert expected_error in actual_error



@then('I verify that a password error message "{expected_error}" is displayed')
def step_verify_password_error_message(context, expected_error):
    actual_error = context.login_page.get_error_message()
    print(expected_error,"------" , actual_error)
    assert expected_error in actual_error



@then("I confirm to remain on login page")
def step_verify_remain_on_login_page(context):
    current_url = context.driver.current_url
    assert "/login" in current_url or "login" in current_url.lower(), (
        f"User navigated away from login page. Current URL: {current_url}"
    )
