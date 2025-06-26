import json
import time
import pytest
from pages.signup_page import SignupPage

#load configuration from config.json file
with open("config.json") as config_file:
    config=json.load(config_file)


def test_signup_function(driver):
    driver.get(config["base_url"])
    #get credentials
    username = config["signup"]["email"]
    newpassword = config["signup"]["newpassword"]
    confirm_password = config["signup"]["confirmpassword"]
   
    # Initialize signup page and perform signup
    signup=SignupPage(driver)
    signup.signup(username,newpassword,confirm_password)
   

@pytest.mark.usefixtures("driver")
def test_signup_error_messages_validation(driver):
    username = config["signup"]["email2"]

    # Initialize forgot password page
    driver.get(config["base_url"])
    signup=SignupPage(driver)
    signup.signup_open()
    # 1. Click submit without entering email
    error_msg = signup.submit_without_email()
    print("Error message for empty email submit:", error_msg)
    assert "email is required" in error_msg.lower()  # Adjust as per actual error

    # 2. Enter email, click continue, enter invalid OTP
    invalid_otp = "000000"
    error_msg_otp = signup.submit_invalid_otp(username, invalid_otp)
    time.sleep(5)
    print("Error message for invalid OTP:", error_msg_otp)

    # 3.capturing error messages for password fields
    errors = signup.submit_password_with_missing_confirm(username, "123")
    print("Error messages for password fields:", errors)
    
@pytest.mark.usefixtures("driver")
def test_signup_email_error_messages(driver):
    # 1. Existing email
    driver.get(config["base_url"])
    signup=SignupPage(driver)
    signup.signup_open()
    existing_email = "vamshinamile22@gmail.com"  # Replace with an actual registered email
    signup.enter_email_and_continue(existing_email)
    error_msg = signup.get_email_error_message()
    print("Error for existing email:", error_msg)
    assert "your account already exists please sign-in" in error_msg.lower()  # Adjust as per your actual error message
    
    