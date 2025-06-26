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



@pytest.mark.usefixtures("driver")
def test_forgotpassword_non_existing_email_error(driver):
    driver.get(config["base_url"])
    forgotpass = Forgotpassword(driver)
    username = config["forgotpassword"]["non_existing_email"]
    # Test with empty email
    error_text = forgotpass.forgotpassword_non_existing_email(username)
    assert "user does not exist" in error_text.lower()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_error_messages_validation(driver):
    driver.get(config["base_url"])
    username = config["forgotpassword"]["email"]

    # Initialize forgot password page
    forgotpass = Forgotpassword(driver)
    # 1. Click submit without entering email
    error_msg = forgotpass.submit_without_email()
    print("Error message for empty email submit:", error_msg)
    assert "email is required" in error_msg.lower()  # Adjust as per actual error

    # 2. Enter email, click continue, enter invalid OTP
    invalid_otp = "000000"
    error_msg_otp = forgotpass.submit_invalid_otp(username, invalid_otp)
    print("Error message for invalid OTP:", error_msg_otp)
    assert "invalid otp" in error_msg_otp.lower()  

    # 3.capturing error messages for password fields
    errors = forgotpass.submit_password_with_missing_confirm(username, "123")
    print("Error messages for password fields:", errors)
    assert any("Password must be at least 8 characters long" in e.lower() or "don't match" in e.lower() for e in errors)  # Adjust as per actual error