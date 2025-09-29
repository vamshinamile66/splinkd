import json
import time
import pytest
from pages.signup_page import SignupPage

#load configuration from config.json file
with open("config.json") as config_file:
    config=json.load(config_file)
    signup_value = config["signup"]
# email-Replace placeholder with dynamic value
timestamp = int(time.time())
dynamic_email = f"ottsi{timestamp}@otsi.co.in"
signup_value['email'] = dynamic_email

@pytest.mark.usefixtures("driver")
def test_signup_mandate_email_field_validation(driver):
    driver.get(config["base_url"])
    signup=SignupPage(driver)
    signup.click_signup_link()
    signup.click_continue_button_for_signup()
    signup.validations_capture()
#valid email check-123
@pytest.mark.usefixtures("driver")
def test_signup_email_field_validation1(driver):
    signup=SignupPage(driver)
    invalid_email1=config["signup"]["invalid_email1"]
    signup.create_username(invalid_email1)
    signup.click_continue_button_for_signup()
    signup.validations_capture()
#valid email check test@test
@pytest.mark.usefixtures("driver")
def test_signup_email_field_validation2(driver):
    signup=SignupPage(driver)
    signup.clear_field(signup.username_input)
    invalid_email2=config["signup"]["invalid_email2"]
    signup.create_username(invalid_email2)
    signup.click_continue_button_for_signup()
    signup.validations_capture()

#check with existing email
@pytest.mark.usefixtures("driver")
def test_signup_email_field_validation3(driver):
    existing_email = config["signup"]["existing_email"]
    signup=SignupPage(driver)
    signup.clear_field(signup.username_input)
    signup.create_username(existing_email)
    signup.click_continue_button_for_signup()
    signup.toast_message("exists")
#check otp toast message
@pytest.mark.usefixtures("driver")
def test_signup_email_submit_toast_message_validation(driver):
    signup=SignupPage(driver)
    username = signup_value['email']
    signup.clear_field(signup.username_input)
    signup.create_username(username)
    signup.click_continue_button()
    signup.toast_message("Sent")


#check otp mandate field validation
@pytest.mark.usefixtures("driver")
def test_signup_otp_mandate_field_validation(driver):
    signup=SignupPage(driver)
    driver.get(config["base_url"])
    signup.click_signup_link()
    time.sleep(2)
    signup.click_continue_button()
    signup.validations_capture()
#enter alphaets in otp field
@pytest.mark.usefixtures("driver")
def test_signup_otp_field_validation_with_alphabets(driver):
    signup=SignupPage(driver)
    alpha_otp = config["signup"]["alpha_otp"]
    username = signup_value['email']
    driver.get(config["base_url"])
    signup.click_signup_link()
    signup.clear_field_signup(signup.username_input)
    time.sleep(1)
    signup.create_username(username)
    signup.click_continue_button()
    signup.create_otp_field(alpha_otp)
    signup.click_continue_button()
    signup.validations_capture()
# #enter less than 6 digits in otp field
@pytest.mark.usefixtures("driver")
def test_signup_otp_field_validation_with_less_numbers(driver):
    signup=SignupPage(driver)
    driver.get(config["base_url"])
    username = signup_value['email']
    signup.click_signup_link()
    signup.clear_field_signup(signup.username_input)
    time.sleep(1)
    signup.create_username(username)
    signup.click_continue_button()
    less_otp = config["signup"]["less_otp"]
    signup.create_otp_field(less_otp)
    signup.click_continue_button()
    signup.validations_capture()
# #enter invalid otp"invalid_otp":"123456",
@pytest.mark.usefixtures("driver")
def test_signup_otp_field_validation_with_incorrect_otp(driver):
    signup=SignupPage(driver)
    invalid_otp = config["signup"]["incorrect_otp"]
    driver.get(config["base_url"])
    username = signup_value['email']
    signup.click_signup_link()
    signup.clear_field_signup(signup.username_input)
    time.sleep(1)
    signup.create_username(username)
    signup.click_continue_button()
    signup.create_otp_field(invalid_otp)
    signup.click_continue_button()
    signup.toast_message("Invalid")

# enter valid otp check otp success toast message
@pytest.mark.usefixtures("driver")
def test_signup_otp_field_validation_with_valid_otp_success_toast(driver):
    signup=SignupPage(driver)
    username = signup_value['email']
    captch_url= config["captch_url"]
    driver.get(config["base_url"])
    signup.click_signup_link()
    signup.clear_field_signup(signup.username_input)
    time.sleep(1)
    signup.create_username(username)
    signup.click_continue_button()
    signup.capture_otp_and_send_otp(captch_url,username)
    signup.click_continue_button()
    signup.toast_message("successfully")
##check Otp is disabled or not initially
@pytest.mark.usefixtures("driver")
def test_signup_is__resend_otp_timer_displayed(driver):
    driver.get(config["base_url"])
    username = signup_value['email']
    signup = SignupPage(driver)
    signup.click_signup_link()
    signup.clear_field_signup(signup.username_input)
    signup.create_username(username)
    signup.click_continue_button()
    signup.check_resend_otp_timer()
@pytest.mark.usefixtures("driver")
def test_signup_is__resend_otp_click_able_after_timer_completed(driver):
    signup = SignupPage(driver)
    signup.check_resend_otp_clickable()

# check resend otp functionality in signup page
@pytest.mark.usefixtures("driver")
def test_signup__resend_function(driver):
    driver.get(config["base_url"])
    username = signup_value['email']
    captch_url= config["captch_url"]
    # Initialize signup page and perform signup
    signup=SignupPage(driver)
    signup.click_signup_link()
    signup.clear_field_signup(signup.username_input)
    time.sleep(1)
    signup.create_username(username)
    signup.click_continue_button()
    time.sleep(35)
    signup.click_resend_otp_link()
    time.sleep(2)
    signup.capture_otp_and_send_otp(captch_url,username)
    signup.click_continue_button()
    signup.toast_message("successfully")

@pytest.mark.usefixtures("driver")
def test_signup_check_entered_email_is_displayed_set_screen(driver):
     signup = SignupPage(driver)
     displayed_email=signup.get_displayed_email()
     entered_email=signup_value['email']
     # Step 3: Compare
     assert displayed_email == entered_email, (
        f"Email mismatch! Entered: {entered_email}, Displayed: {displayed_email}"
    )
     print("✅ Email displayed correctly after navigation to set password screen.")

# #---------------------------step 3 set password screen-------------------------
@pytest.mark.usefixtures("driver")
def test_signup_set_password_mandatory_fields_message(driver):
    driver.get(config["base_url"])
    captch_url = config["captch_url"]
    username = signup_value['email']
    signup = SignupPage(driver)
    signup.click_signup_link()
    signup.clear_field_signup(signup.username_input)
    signup.create_username(username)
    signup.click_continue_button()
    signup.capture_otp_and_send_otp(captch_url, username)
    signup.click_continue_button()
    # Leave password fields blank and submit
    signup.click_continue_button_for_signup()
    # Capture validations
    signup.validations_capture()


@pytest.mark.usefixtures("driver")
def test_signup_set_min_validation_error(driver):
    signup = SignupPage(driver)
    newpassword = config["signup"]["set_min"]
    confirmpassword = config["signup"]["set_min"]
    
    signup.clear_field_signup(signup.password_input)
    time.sleep(1)
    signup.create_password(newpassword)
    signup.clear_field_signup(signup.confirmpassword_input)
    time.sleep(1)
    signup.create_confirm_password(confirmpassword)

    signup.click_continue_button_for_signup()
    signup.validations_capture()


@pytest.mark.usefixtures("driver")
def test_signup_set_num_validation_error(driver):
    newpassword = config["signup"]["set_num"]
    confirmpassword = config["signup"]["set_num"]

    signup = SignupPage(driver)
    signup.clear_field_signup(signup.password_input)
    time.sleep(1)
    signup.create_password(newpassword)
    signup.clear_field_signup(signup.confirmpassword_input)
    time.sleep(1)
    signup.create_confirm_password(confirmpassword)
    signup.click_continue_button_for_signup()

    signup.validations_capture()


@pytest.mark.usefixtures("driver")
def test_signup_set_alpha_validation_error(driver):
    newpassword = config["signup"]["set_alpha"]
    confirmpassword = config["signup"]["set_alpha"]

    signup = SignupPage(driver)

    signup.clear_field_signup(signup.password_input)
    time.sleep(1)
    signup.create_password(newpassword)
    signup.clear_field_signup(signup.confirmpassword_input)
    time.sleep(1)
    signup.create_confirm_password(confirmpassword)

    signup.click_continue_button_for_signup()

    signup.validations_capture()


@pytest.mark.usefixtures("driver")
def test_signup_set_sym_validation_error(driver):
    newpassword = config["signup"]["set_sym"]
    confirmpassword = config["signup"]["set_sym"]

    signup = SignupPage(driver)
    signup.clear_field_signup(signup.password_input)
    time.sleep(1)
    signup.create_password(newpassword)
    signup.clear_field_signup(signup.confirmpassword_input)
    time.sleep(1)
    signup.create_confirm_password(confirmpassword)
    signup.click_continue_button_for_signup()

    signup.validations_capture()

@pytest.mark.usefixtures("driver")
def test_signup_set_min_pass_validation_error(driver):
    """Validate error when signup password length is less than minimum required."""
    newpassword = config["signup"]["set_min_pass"]
    confirmpassword = config["signup"]["set_min_pass"]

    signup = SignupPage(driver)
    # Set weak password
    signup.clear_field_signup(signup.password_input)
    time.sleep(1)
    signup.create_password(newpassword)
    signup.clear_field_signup(signup.confirmpassword_input)
    time.sleep(1)
    signup.create_confirm_password(confirmpassword)

    signup.click_continue_button_for_signup()

    # Capture validation error
    signup.validations_capture()


@pytest.mark.usefixtures("driver")
def test_signup_new_and_confirm_pass_mismatch_validation_error(driver):
    """Validate error when signup new password and confirm password do not match."""
    newpassword = config["signup"]["mismatch_new"]
    confirmpassword = config["signup"]["mismatch_conf"]
    signup = SignupPage(driver)
    # Enter mismatched passwords
    signup.clear_field_signup(signup.password_input)
    time.sleep(1)
    signup.create_password(newpassword)
    signup.clear_field_signup(signup.confirmpassword_input)
    time.sleep(1)
    signup.create_confirm_password(confirmpassword)
    signup.click_continue_button_for_signup()

    # Capture validation error
    signup.validations_capture()

@pytest.mark.usefixtures("driver")
def test_signup_function(driver):
    driver.get(config["base_url"])
    username = signup_value['email']
    newpassword = config["signup"]["newpassword"]
    confirm_password = config["signup"]["confirmpassword"]
    captch_url= config["captch_url"]
    # Initialize signup page and perform signup
    signup=SignupPage(driver)
    signup.click_signup_link()
    signup.clear_field_signup(signup.username_input)
    time.sleep(1)
    signup.create_username(username)
    signup.click_continue_button()
    signup.capture_otp_and_send_otp(captch_url,username)
    signup.click_continue_button()
    signup.create_password(newpassword)
    signup.create_confirm_password(confirm_password)
    signup.click_continue_button_for_signup()
    if signup.is_logged_in():
        print("✅User is successfully logged In")
    else:
        assert False, "⚠️ User login failed after signup"

@pytest.mark.usefixtures("driver")
def test_is_profile_email_matched_function(driver):
    signup=SignupPage(driver)
    username = signup_value['email']
    signup.click_profile_toggle_button()
    if signup.capture_and_compare_profile_email(username):
        print("✅Profile email matches the signup email.")
    else:
        assert False, "⚠️ Profile email does not match the signup email."

def test_logout_function(driver):
    signup=SignupPage(driver)
    signup.logout()
    time.sleep(2)
       
@pytest.mark.usefixtures("driver")
def test_new_signed_up_user_is_able_to_login(driver):
    """Test login with newly created signup credentials"""
    driver.get(config["base_url"])
    username = signup_value['email']
    newpassword = config["signup"]["newpassword"]
    signup=SignupPage(driver)
    signup.clear_field(signup.username_input)
    time.sleep(1)
    signup.create_username(username)
    signup.clear_field(signup.password_input)
    time.sleep(1)
    signup.create_password(newpassword)
    signup.click_login_button()
    time.sleep(4)
    if signup.is_logged_in():
        print("✅Login successfull with newly created credentials")
    else:
        assert False, "⚠️ Login failed with with newly created credentials"
    signup.click_profile_toggle_button()
    signup.logout()
    time.sleep(2)