from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from features.configs.config_reader import ConfigReader

def create_driver():
    config = ConfigReader()
    browser = config.get_browser()

    if browser == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    return driver
