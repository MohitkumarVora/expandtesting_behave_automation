from utils.driver_factory import create_driver
from features.configs.config_reader import ConfigReader
from utils.screenshot_utils import take_screenshot
import allure


def before_all(context):
    """
    Runs once before the entire test suite
    """
    context.config_reader = ConfigReader()


def before_scenario(context, scenario):
    """
    Runs before each scenario
    """
    context.driver = create_driver()

    if hasattr(context, "config_reader"):
        base_url = context.config_reader.get_base_url()
        context.driver.get(base_url)


def after_step(context, step):
    if step.status == "failed":
        screenshot_path = take_screenshot(context.driver, step.name)

        if screenshot_path:
            try:
                allure.attach.file(
                    screenshot_path,
                    name=step.name,
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"[WARN] Allure attach failed: {e}")


def after_scenario(context, scenario):
    """
    Runs after each scenario
    """
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
