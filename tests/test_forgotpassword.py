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
validations = config["validations"]

# ##-------------------------------step-1 email screen--------------------------
@pytest.mark.usefixtures("driver")
def test_forgotpassword_email_madandate_error(driver):
    driver.get(config["base_url"])
    forgotpass = Forgotpassword(driver)
    forgotpass.click_forgot_password_link()
    time.sleep(1)
    forgotpass.click_continue_button()
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_email_field_validation1_error(driver):
    forgotpass = Forgotpassword(driver)   
    forgotpass.clear_field(forgotpass.username_input)
    forgotpass.create_username(validations["Number"])
    forgotpass.click_continue_button()
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_email_field_validation2_error(driver):
    forgotpass = Forgotpassword(driver)
    forgotpass.clear_field(forgotpass.username_input)
    forgotpass.create_username(validations["incorrect_email"])
    forgotpass.click_continue_button()
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_email_field_validation3_error(driver):
    forgotpass = Forgotpassword(driver)
    forgotpass.clear_field(forgotpass.username_input)
    forgotpass.create_username(validations["alphabit"])
    forgotpass.click_continue_button()
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_non_existing_email_error(driver):
    forgotpass = Forgotpassword(driver)
    username = config["forgotpassword"]["non_existing_email"]
    forgotpass.clear_field(forgotpass.username_input)
    forgotpass.create_username(username)
    forgotpass.click_continue_button()
    forgotpass.toast_message("User does not exist")
#-------------------------------step-2 OTP screen--------------------------------
@pytest.mark.usefixtures("driver")
def test_check_label__name_displayed_in_description(driver):
    forgotpass = Forgotpassword(driver)
    result = forgotpass.compare_label_with_description()
    assert result, "Label text not found in description text!"

@pytest.mark.usefixtures("driver")
def test_forgotpassword_OTP_mandate_field_validation(driver):
    forgotpass = Forgotpassword(driver)
    username = config["forgotpassword"]["email_5times"]
    forgotpass.clear_field(forgotpass.username_input)
    forgotpass.create_username(username)
    forgotpass.click_continue_button()
    time.sleep(2)
    forgotpass.verify_otp_text_and_click_continue()
    forgotpass.validations_capture()
    
@pytest.mark.usefixtures("driver")
def test_forgotpassword_invalid_otp1_error(driver):
    forgotpass = Forgotpassword(driver)
    invalid_otp = config["forgotpassword"]["static_invalid_otp_number"]
    forgotpass.enter_otp(invalid_otp)
    forgotpass.click_continue_button()
    forgotpass.toast_message("Invalid")

@pytest.mark.usefixtures("driver")
def test_forgotpassword_invalid_otp2_error(driver):
    forgotpass = Forgotpassword(driver)
    invalid_otp = config["forgotpassword"]["invalid_otp_alpha"]
    forgotpass.clear_field(forgotpass.OTP_input)
    forgotpass.enter_otp(invalid_otp)
    forgotpass.click_continue_button()
    forgotpass.toast_message("Invalid")

@pytest.mark.usefixtures("driver")
def test_forgotpassword_otp_success_message(driver):
    driver.get(config["base_url"])
    captch_url= config["captch_url"]
    username = config["forgotpassword"]["email_5times"]
    forgotpass = Forgotpassword(driver)
    forgotpass.click_forgot_password_link()
    forgotpass.create_username(username)
    forgotpass.click_continu_button()
    time.sleep(2)
    forgotpass.capture_otp(username,captch_url)
    time.sleep(3)
    forgotpass.toast_message("OTP is verified successfully")

@pytest.mark.usefixtures("driver")
def test_forgotpassword_resend_capture_success_message(driver):
    driver.get(config["base_url"])
    username = config["forgotpassword"]["email_5times"]
    forgotpass = Forgotpassword(driver)
    forgotpass.click_forgot_password_link()
    forgotpass.create_username(username)
    forgotpass.click_continue_button()
    print("waiting for 30 sec")
    time.sleep(31)
    forgotpass.click_resend_otp_link()
    forgotpass.toast_message("verify")

@pytest.mark.usefixtures("driver")
def test_forgotpassword_resend_function(driver):
    driver.get(config["base_url"])
    captch_url= config["captch_url"]
    username = config["forgotpassword"]["email_5times"]
    forgotpass = Forgotpassword(driver)
    forgotpass.click_forgot_password_link()
    forgotpass.create_username(username)
    forgotpass.click_continue_button()
    print("waiting for 30 sec")
    time.sleep(31)
    forgotpass.click_resend_otp_link()
    time.sleep(3)
    forgotpass.capture_otp(username,captch_url)
    time.sleep(1)
    title, desc = forgotpass.get_toast_message()
    assert title == "SUCCESS", f"Expected SUCCESS but got {title}, desc: {desc}"
    

@pytest.mark.usefixtures("driver")
def test_forgotpassword_resend_Old_OTP_error(driver):
    driver.get(config["base_url"])
    captch_url= config["captch_url"]
    # Get credentials from config file
    username = config["forgotpassword"]["email_5times"]
    forgotpass = Forgotpassword(driver)
    forgotpass.click_forgot_password_link()
    forgotpass.create_username(username)
    forgotpass.click_continue_button()
    old_otp=forgotpass.capture_otp_and_return_methode(username,captch_url)
    print(f"captured OTP value: {old_otp}")
    time.sleep(31)
    forgotpass.click_resend_otp_link()
    time.sleep(1)
    forgotpass.enter_otp(old_otp)
    forgotpass.click_continu_button()
    forgotpass.toast_message("Invalid")

@pytest.mark.usefixtures("driver")
def test_forgotpassword_invalid_otp_Attempts_more_than_5times_error(driver):
    driver.get(config["base_url"])
    # Get credentials from config file
    username = config["forgotpassword"]["email_5times"]
    invalid_otp=config["forgotpassword"]["static_invalid_otp_number"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    # forgotpass.forgotpassword(username, newpassword, confirmpassword, captch_url)
    forgotpass.click_forgot_password_link()
    forgotpass.submit_invalid_otp(username,invalid_otp)
     # Click continue button 5 times
    forgotpass.click_continue_button(times=6)
    print("Clicked Continue button 6 times")
    time.sleep(2)
    forgotpass.toast_message("Too many failed")

#---------------------------step 3 set password screen-------------------------

@pytest.mark.usefixtures("driver")
def test_forgotpassword_set_password_mandate_fileds_message(driver):
    driver.get(config["base_url"])
    captch_url= config["captch_url"]
    # Get credentials from config file
    username = config["forgotpassword"]["email"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.click_forgot_password_link()
    forgotpass.create_username(username)
    forgotpass.click_continue_button()
    forgotpass.capture_otp(username,captch_url)
    forgotpass.click_submit_button()
    time.sleep(1)
    forgotpass.validations_capture()
    
@pytest.mark.usefixtures("driver")
def test_forgotpassword_set_min_validation_error(driver):
    driver.get(config["base_url"])
    captch_url= config["captch_url"]
    # Get credentials from config file
    username = config["forgotpassword"]["email"]
    newpassword = config["forgotpassword"]["set_min"]
    confirmpassword = config["forgotpassword"]["set_min"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.click_forgot_password_link()
    forgotpass.create_username(username)
    forgotpass.click_continue_button()
    forgotpass.capture_otp(username,captch_url)
    forgotpass.create_new_password(newpassword)
    forgotpass.create_confirm_password(confirmpassword)
    forgotpass.click_submit_button()
    time.sleep(1)
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_set_num_validation_error(driver):
    # Get credentials from config file
    newpassword = config["forgotpassword"]["set_num"]
    confirmpassword = config["forgotpassword"]["set_num"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.clear_field(forgotpass.newpassword_input)
    forgotpass.create_new_password(newpassword)
    time.sleep(1)
    forgotpass.clear_field(forgotpass.confirmpassword_input)
    time.sleep(1)
    forgotpass.create_confirm_password(confirmpassword)
    forgotpass.click_submit_button()
    time.sleep(1)
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_set_alpha_validation_error(driver):
    # Get credentials from config file
    newpassword = config["forgotpassword"]["set_alpha"]
    confirmpassword = config["forgotpassword"]["set_alpha"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.clear_field(forgotpass.newpassword_input)
    forgotpass.create_new_password(newpassword)
    time.sleep(1)
    forgotpass.clear_field(forgotpass.confirmpassword_input)
    time.sleep(1)
    forgotpass.create_confirm_password(confirmpassword)
    forgotpass.click_submit_button()
    time.sleep(1)
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_set_sym_validation_error(driver):
    # Get credentials from config file
    newpassword = config["forgotpassword"]["set_sym"]
    confirmpassword = config["forgotpassword"]["set_sym"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.clear_field(forgotpass.newpassword_input)
    forgotpass.create_new_password(newpassword)
    time.sleep(1)
    forgotpass.clear_field(forgotpass.confirmpassword_input)
    time.sleep(1)
    forgotpass.create_confirm_password(confirmpassword)
    forgotpass.click_submit_button()
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_set_min_pass_validation_error(driver):
    # Get credentials from config file
    newpassword = config["forgotpassword"]["set_min_pass"]
    confirmpassword = config["forgotpassword"]["set_min_pass"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.clear_field(forgotpass.newpassword_input)
    forgotpass.create_new_password(newpassword)
    time.sleep(1)
    forgotpass.clear_field(forgotpass.confirmpassword_input)
    time.sleep(1)
    forgotpass.create_confirm_password(confirmpassword)
    forgotpass.click_submit_button()
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_new_and_confirm_pass_mismatch_validation_error(driver):
    # Get credentials from config file
    newpassword = config["forgotpassword"]["mismatch_new"]
    confirmpassword = config["forgotpassword"]["mismatch_conf"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.clear_field(forgotpass.newpassword_input)
    forgotpass.create_new_password(newpassword)
    time.sleep(1)
    forgotpass.clear_field(forgotpass.confirmpassword_input)
    time.sleep(1)
    forgotpass.create_confirm_password(confirmpassword)
    forgotpass.click_submit_button()
    forgotpass.validations_capture()

@pytest.mark.usefixtures("driver")
def test_forgotpassword_function(driver):
    driver.get(config["base_url"])
    captch_url= config["captch_url"]
    # Get credentials from config file
    username = config["forgotpassword"]["email"]
    newpassword = config["forgotpassword"]["newpassword"]
    confirmpassword = config["forgotpassword"]["confirmpassword"]
    # Initialize forgot page and perform forgotpassword
    forgotpass = Forgotpassword(driver)
    forgotpass.click_forgot_password_link()
    forgotpass.create_username(username)
    forgotpass.click_continue_button()
    forgotpass.capture_otp(username,captch_url)
    forgotpass.create_new_password(newpassword)
    forgotpass.create_confirm_password(confirmpassword)
    forgotpass.click_submit_button()
    time.sleep(1)
    forgotpass.toast_message("Password Updated Successfully")

@pytest.mark.usefixtures("driver")
def test_updated_password_login(driver):
    """Test login with updated password."""
    driver.get(config["base_url"])
    username = config["forgotpassword"]["email"]
    password = config["forgotpassword"]["newpassword"]
    forgotpass = Forgotpassword(driver)
    forgotpass.create_username(username)
    forgotpass.create_password(password)
    forgotpass.click_login_button()
    time.sleep(4)
    if forgotpass.is_logged_in():
        print("✅ User is able to login with updated password")
    else:
        assert False, "Login failed with updated password"
    forgotpass.signout()




#-----------------------this test case take 10 mins so disabled-------------------------
# @pytest.mark.usefixtures("driver")
# def test_forgotpassword_after_10mins_otp_validation_error(driver):
#     driver.get(config["base_url"])
#     captch_url= config["captch_url"]
#     # Get credentials from config file
#     username = config["forgotpassword"]["email"]
#    # Initialize forgot page and perform forgotpassword
#     forgotpass = Forgotpassword(driver)
#     # forgotpass.forgotpassword(username, newpassword, confirmpassword, captch_url)
#     forgotpass.click_forgot_password_link()
#     forgotpass.create_username(username)
#     forgotpass.click_continue_button()
#     time.sleep(610)
#     forgotpass.capture_otp(username,captch_url)
#     forgotpass.toast_message("Invalid")
   
    
    

