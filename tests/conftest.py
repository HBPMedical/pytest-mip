import pytest
import os
from datetime import datetime
from py.xml import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import project_parameters


"""Define fixtures that will be shared among all federation tests."""


# set up default of desired dpi for screenshots of failed tests
DESIRED_DPI = 1


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


@pytest.fixture(scope="class")
def selenium_driver(request):
    """Set up selenium chrome webdriver fixture."""
    _driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=set_chrome_options()
    )
    _driver.maximize_window()
    _driver.implicitly_wait(20)
    _driver.get(request.param)
    request.cls.driver = _driver
    yield request.cls.driver
    request.cls.driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add screenshot to html report for failed tests."""
    timestamp = datetime.now().strftime("%H-%M-%S")
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    report.description = getattr(item.function, "__doc__", "")
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        print(item.funcargs)
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs["selenium_driver"]
            report_directory = os.path.dirname(item.config.option.htmlpath)
            img_name = (
                report.nodeid.replace("::", "_")
                .replace(".py", "")
                .replace("://", "_")
                .replace("[", "_")
                .replace("/]", "")
                .replace("]", "")
                + "_"
                + timestamp
                + ".png"
            )
            img_path = os.path.join(report_directory, img_name)
            print("Save screenshot to: %s" % img_path)
            driver.save_screenshot(img_path)
            if img_path:
                html = (
                    '<div><img src ="%s" alt="screenshot" style="height:auto;width:auto;max-width:%s;max-height:%s;" onclick ="window.open(this.src)" align="right"/></div>'
                    % (img_name, "500px", "500px")
                )
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_results_table_header(cells):
    """Customize results table header columns in pytest-html report."""
    cells.insert(2, html.th("Description"))
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    """Customize results table row columns in pytest-html report."""
    cells.insert(2, html.td(getattr(report, "description", "")))
    cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop()


def pytest_html_report_title(report):
    """Set report title."""
    report.title = "Integration Tests of MIP Federations"
