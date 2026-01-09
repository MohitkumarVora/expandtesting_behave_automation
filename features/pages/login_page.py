from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class LoginPage(BasePage):

    # -------- Locators --------
    link_test_login_page = (By.LINK_TEXT, "Test Login Page")
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_btn = (By.XPATH, "//button[text()='Login']")
    success_message = (By.XPATH, "//div[(@id='flash') and contains(@class,'success')]")
    error_message = (By.XPATH, "//div[@id='flash']/b")
    logout_btn = (By.XPATH, "//a[@href='/logout']")

    # -------- Page Actions --------
    def open(self):
        """Open Test Login Page from home"""
        self.click(self.link_test_login_page)

    def enter_username(self, username):
        self.type(self.username_input, username)

    def enter_password(self, password):
        self.type(self.password_input, password)

    def click_login(self):
        self.click(self.login_btn)

    def login(self, user, pwd):
        """Single-step login (optional usage)"""
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_login()

    # -------- Validations --------
    def get_success_message(self):
        return self.get_text(self.success_message)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def is_logout_button_displayed(self):
        return self.is_element_visible(self.logout_btn)
