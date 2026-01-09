from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.configs.config_reader import ConfigReader


class BasePage:
    """
    BasePage contains all common reusable Selenium actions.
    All Page Object classes should inherit from this class.
    """

    def __init__(self, driver):
        """
        Constructor to initialize WebDriver and explicit wait.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver
        config = ConfigReader()
        explicit_wait = config.get_explicit_wait()
        self.wait = WebDriverWait(driver, explicit_wait)

    def wait_for_element_visible(self, locator):
        """
        Wait until the element is present in DOM and visible on UI.

        :param locator: Tuple(By, locator)
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        """
        Wait until the element is visible and enabled so it can be clicked.

        :param locator: Tuple(By, locator)
        :return: WebElement
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """
        Click on an element.
        First attempts normal Selenium click.
        Falls back to JavaScript click if normal click fails.

        :param locator: Tuple(By, locator)
        """
        element = self.wait_for_element_clickable(locator)

        # Scroll element into view to avoid interception issues
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        try:
            element.click()
        except:
            # JS click fallback for stubborn elements
            self.driver.execute_script("arguments[0].click();", element)

    def double_click_action(self, locator):
        """
        Perform double-click action on an element.

        :param locator: Tuple(By, locator)
        """
        element = self.wait_for_element_visible(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click_action(self, locator):
        """
        Perform right-click (context click) on an element.

        :param locator: Tuple(By, locator)
        """
        element = self.wait_for_element_visible(locator)
        ActionChains(self.driver).context_click(element).perform()

    def type(self, locator, text):
        """
        Clear existing text and type new text into input field.

        :param locator: Tuple(By, locator)
        :param text: Text to be entered
        """
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Get visible text from an element.

        :param locator: Tuple(By, locator)
        :return: Text value of the element
        """
        return self.wait_for_element_visible(locator).text

    def get_attribute(self, locator, attribute):
        """
        Get attribute value of an element.

        :param locator: Tuple(By, locator)
        :param attribute: Attribute name
        :return: Attribute value
        """
        return self.wait_for_element_visible(locator).get_attribute(attribute)

    def scroll_down(self, pixels=300):
        """
        Scroll down the page by given pixels.

        :param pixels: Number of pixels to scroll (default 300)
        """
        self.driver.execute_script(f"window.scrollBy(0, {pixels})")

    def is_element_visible(self, locator):
        """
        Check if element is visible on UI.
        Returns True if visible, False otherwise.

        :param locator: Tuple(By, locator)
        :return: Boolean
        """
        try:
            self.wait_for_element_visible(locator)
            return True
        except:
            return False
    
    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))
    