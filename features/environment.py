from utils.driver_factory import create_driver
from features.configs.config_reader import ConfigReader


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

    base_url = context.config_reader.get_base_url()
    context.driver.get(base_url)


def after_scenario(context, scenario):
    """
    Runs after each scenario
    """
    if context.driver:
        context.driver.quit()
