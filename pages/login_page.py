from selenium.webdriver.common.by import By
from utils.config_reader import get_base_url

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.XPATH, "//button[text()='Login']")

    def open(self):
        self.driver.get(f"{get_base_url()}/login")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
