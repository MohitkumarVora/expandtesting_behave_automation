import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "config.ini"))

def get_browser():
    return config.get("DEFAULT", "browser", fallback="chrome").lower()

def get_base_url():
    return config.get("DEFAULT", "base_url")
