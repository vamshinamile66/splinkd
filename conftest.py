import json
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
# Load JSON file
with open("config.json") as configfile:
    config = json.load(configfile)

@pytest.fixture(scope="session")
def driver():
    browser = config["browser"].strip().lower()
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
    elif browser == "headless":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Store pytest_html in config for use in hooks
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

#screenshot on failure

# Attach screenshot in report for failed tests
from pytest_html import extras

import json
import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Load config.json
with open("config.json") as configfile:
    config = json.load(configfile)


@pytest.fixture(scope="session")
def driver():
    browser = config["browser"].strip().lower()
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
    elif browser == "headless":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# --------------------------
# Hook to attach screenshots
# from pytest_html import extras

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get("driver", None)
#         if driver:
#             screenshot_dir = "screenshots"
#             os.makedirs(screenshot_dir, exist_ok=True)

#             screenshot_file = os.path.join(screenshot_dir, f"{item.name}.png")
#             driver.save_screenshot(screenshot_file)

#             if item.config.pluginmanager.hasplugin("html"):  # ✅ FIXED
#                 extra = getattr(rep, "extra", [])
#                 extra.append(extras.image(screenshot_file))
#                 rep.extra = extra