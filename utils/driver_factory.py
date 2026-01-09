from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from features.configs.config_reader import ConfigReader


def create_driver():
    config = ConfigReader()
    browser = config.get_browser()

    if browser == "chrome":
        chrome_options = ChromeOptions()

        # ✅ Incognito mode
        chrome_options.add_argument("--incognito")

        # ✅ Recommended stability options
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )

    elif browser == "firefox":
        firefox_options = FirefoxOptions()

        # ✅ Firefox private mode (optional)
        firefox_options.add_argument("-private")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.delete_all_cookies()
    driver.implicitly_wait(10)

    return driver
