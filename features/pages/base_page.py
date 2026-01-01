from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.configs.config_reader import ConfigReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        config = ConfigReader()
        explicit_wait = config.get_explicit_wait()
        self.wait = WebDriverWait(driver, explicit_wait)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def double_click_action(self, locator):
        element = self.wait_for_element_visible(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click_action(self, locator):
        element = self.wait_for_element_visible(locator)
        ActionChains(self.driver).context_click(element).perform()

    def type(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text

    def get_attribute(self, locator, attribute):
        return self.wait_for_element_visible(locator).get_attribute(attribute)

    def scroll_down(self, pixels=300):
        self.driver.execute_script(f"window.scrollBy(0, {pixels})")
