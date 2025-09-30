import json
import pytest
import time
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)
validations = config["validations"]
# @pytest.mark.usefixtures("driver")
# def test_mandate_field_validation_errors(driver):
#     driver.get(config["base_url"])
#     login_page = LoginPage(driver)
#     time.sleep(4)
#     login_page.click_login_button()
#     actual_errors = login_page.validations_capture()
#     expected_errors = {
#             "Email": "Email is required",
#             "Password": "Password is required"
#         }
#     assert login_page.compare_errors(expected_errors, actual_errors), \
#             f"Validation errors mismatch!\nExpected: {expected_errors}\nGot: {actual_errors}"

# def test_check_forgot_password_link_is_displayed(driver):
#     login_page = LoginPage(driver)
#     assert login_page.is_forgot_password_displayed(), "'Forgot Password?' button not visible on login screen"

# def test_check_signup_link_is_displayed(driver):
#     login_page = LoginPage(driver)
#     assert login_page.is_signup_link_displayed(), "'Sign Up' link is not visible on login screen"

# @pytest.mark.usefixtures("driver")
# def test_correct_username_incorrect_password_validation_error(driver):
#     driver.get(config["base_url"])
#     login_page = LoginPage(driver)
#     username = config["username"]
#     login_page.create_username(username)
#     login_page.create_password("Qa@1234")
#     login_page.click_login_button()
#     time.sleep(1)
#     login_page.toast_message("Invalid")

# @pytest.mark.usefixtures("driver")
# def test_incorrect_username_correct_password_validation_error(driver):
#     driver.get(config["base_url"])
#     login_page = LoginPage(driver)
#     password = config["password"]
#     login_page.create_username("dummy@gmail.com")
#     login_page.create_password(password)
#     login_page.click_login_button()
#     time.sleep(1)
#     login_page.toast_message("please Sign Up")

@pytest.mark.usefixtures("driver")
def test_login_correct_username_correct_password(driver):
    """Test login with correct username and correct password."""
    driver.get(config["base_url"])
    username = config["username"]
    password = config["password"]
    login_page = LoginPage(driver)
    login_page.clear_field(login_page.username_input)
    time.sleep(1)
    login_page.create_username(username)
    login_page.clear_field(login_page.password_input)
    time.sleep(1)
    login_page.create_password(password)
    login_page.click_login_button()
    time.sleep(4)
    if login_page.is_logged_in():
        print("✅ Login test with correct username and correct password executed successfully!")
    else:
        assert False, "Login failed with correct username and correct password"

   
