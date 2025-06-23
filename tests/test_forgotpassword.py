import json
import pytest
import sys
import os
from selenium.webdriver.support import expected_conditions as EC
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.forgotpassword_page import Forgotpassword

# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)
@pytest.mark.usefixtures("driver")
def test_forgotpassword_function(driver):
    driver.get(config["base_url"])
    
    # Get credentials from config file
    username = config["forgotpassword"]["email"]
    newpassword = config["forgotpassword"]["newpassword"]
    confirmpassword = config["forgotpassword"]["confirmpassword"]
    
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.forgotpassword(username, newpassword, confirmpassword)
    time.sleep(5)
def test_forgotpassword_invalid_email(driver):
    forgotpass = Forgotpassword(driver)
    error_message = forgotpass.forgotpassword_invalid_email("notexist@example.com")
    assert "does not exist" in error_message.lower()  # Adjust as per actual error text
    time.sleep(5)  # Wait for any UI updates or transitions