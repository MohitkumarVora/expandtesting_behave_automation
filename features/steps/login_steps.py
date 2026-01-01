from behave import given, when, then
from pages.login_page import LoginPage

@given("user is on login page")
def step_open_login(context):
    context.login = LoginPage(context.driver)
    context.login.open()

@when("user enters valid username and password")
def step_login(context):
    context.login.login("practice", "SuperSecretPassword!")

@then("user should be logged in successfully")
def step_verify(context):
    assert "dashboard" in context.driver.current_url
