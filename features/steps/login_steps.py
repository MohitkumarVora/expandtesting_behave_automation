from behave import given, when, then
from features.pages.login_page import LoginPage


@given("user is on login page")
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when("user enters valid username and password")
def step_login(context):
    context.login_page.login("practice", "SuperSecretPassword!")


@then("user should be logged in successfully")
def step_verify(context):
    assert "/secure" in context.driver.current_url
