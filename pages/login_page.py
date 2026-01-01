from selenium.webdriver.common.by import By
from utils.config_reader import get_base_url

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    link_test_login_page = (By.LINK_TEXT, "Test Login Page")
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.XPATH, "//button[text()='Login']")

    def open(self):
        self.driver.get(self.link_test_login_page)

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
