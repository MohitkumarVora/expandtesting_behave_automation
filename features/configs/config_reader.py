import configparser
import os


class ConfigReader:

    def __init__(self):
        config_path = os.path.join(
            os.path.dirname(__file__),
            "config.ini"
        )
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_base_url(self):
        return self.config.get("app", "base_url")

    def get_browser(self):
        return self.config.get("browser", "name")

    def get_explicit_wait(self):
        return self.config.getint("timeouts", "explicit_wait")

