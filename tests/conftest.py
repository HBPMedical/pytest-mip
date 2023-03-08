import os
from datetime import datetime
from py.xml import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

"""Define fixtures that will be shared among all federation tests."""


# set up default of desired dpi for screenshots of failed tests
DESIRED_DPI = 0.33


def set_chrome_options(desired_dpi=None) -> None:
    """Sets chrome options for Selenium.

    Chrome options for headless browser is enabled.

    Parameters
    ----------
    desired_dpi : float
        Desired dpi for screenshots of failed tests given to
        `--force-device-scale-factor` chrome option flag.
    """
    if not desired_dpi:
        desired_dpi = DESIRED_DPI
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(f"--force-device-scale-factor={desired_dpi}")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


@pytest.fixture(scope="function")
def selenium_driver():
    """Set up selenium chrome webdriver fixture."""
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=set_chrome_options()
    )
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()
