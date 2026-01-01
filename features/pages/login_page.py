from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class LoginPage(BasePage):

    # Locators
    link_test_login_page = (By.LINK_TEXT, "Test Login Page")
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.XPATH, "//button[text()='Login']")

    def open(self):
        self.click(self.link_test_login_page)

    def login(self, user, pwd):
        self.type(self.username, user)
        self.type(self.password, pwd)
        self.click(self.login_btn)
