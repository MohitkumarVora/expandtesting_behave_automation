import allure
from utils.driver_factory import create_driver
from utils.screenshot_utils import take_screenshot

def before_scenario(context, scenario):
    context.driver = create_driver()

def after_step(context, step):
    if step.status == "failed":
        screenshot = take_screenshot(context.driver, step.name)
        allure.attach.file(
            screenshot,
            name=step.name,
            attachment_type=allure.attachment_type.PNG
        )

def after_scenario(context, scenario):
    context.driver.quit()
