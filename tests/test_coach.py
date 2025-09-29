import pytest
import json
import time
from pages.coach_page import CoachPage

with open("config.json") as f:
    config = json.load(f)
coach = config["coach"]
# email-Replace placeholder with dynamic value
timestamp = int(time.time())
dynamic_email = f"coach{timestamp}@otsi.co.in"
coach['email'] = dynamic_email
validations = config["validations"]
#--------------------------onboard coach test cases-----------------------------
@pytest.mark.usefixtures("driver")
def test_click_on_coach_tab(driver):
    page = CoachPage(driver)
    page.click_coach_tab()

@pytest.mark.usefixtures("driver")
def test_click_on_on_board_coach_button(driver):
    page = CoachPage(driver)
    page.click_on_board_coach_button()

def test_onboard_coach_valid_details(driver):
    page = CoachPage(driver)
    page.create_first_name_input(coach["first_name"])
    page.create_last_name_input(coach["last_name"])
    page.click_and_select_dob(coach["year"])
    page.click_select_gender_dropdown()
    page.create_email_input(coach["email"])
    page.create_mobile_input(coach["mobile"])
    page.click_create_button()
    page.toast_message("Coach Onboarding Successful")
#-------------------------------------------------------------------#
@pytest.mark.usefixtures("driver")
def test_existing_email_validation_error(driver):
    page = CoachPage(driver)
    time.sleep(2)
    page.click_on_board_coach_button()
    page.create_first_name_input(coach["first_name"])
    page.create_last_name_input(coach["last_name"])
    page.click_and_select_dob(coach["year"])
    page.click_select_gender_dropdown()
    page.create_email_input(coach["email"])
    page.create_mobile_input(coach["mobile"])
    page.click_create_button()
    page.toast_message("Coach is already onboarded to this academy")
    time.sleep(2)
    page.click_cancel_button()
    time.sleep(1)


@pytest.mark.usefixtures("driver")
def test_mandatory_field_validation_errors(driver):
    page = CoachPage(driver)
    page.click_on_board_coach_button()
    page.click_create_button()
    page.validation_messages()
    page.click_cancel_button()


@pytest.mark.usefixtures("driver")
def test_enter_coach_details_for_validation(driver):
    page = CoachPage(driver)
    page.click_on_board_coach_button()
    page.create_first_name_input(coach["first_name"])
    page.create_last_name_input(coach["last_name"])
    page.click_and_select_dob(coach["year"])
    page.click_select_gender_dropdown()
    page.create_email_input(validations["static_email"])
    page.create_mobile_input(coach["mobile"])

@pytest.mark.usefixtures("driver")
def test_coach_first_name_field_minimum_length_validation(driver):
    page = CoachPage(driver)
    #firt name validation
    page.clear_field(page.coach_first_name_input)
    time.sleep(1)
    page.create_first_name_input(validations["min_value"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_coach_first_name_field_maximum_length_validation(driver):
    page = CoachPage(driver)
    #validate max value
    page.clear_field(page.coach_first_name_input)
    time.sleep(1)
    page.create_first_name_input(validations["max_value"])
    page.click_create_button()
    time.sleep(2)
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_coach_first_name_field_invalid_number_validation(driver):
    page = CoachPage(driver)
    #numeric value
    page.clear_field(page.coach_first_name_input)
    time.sleep(1)
    page.create_first_name_input(validations["Number"])
    page.click_create_button()
    page.validation_messages()

@pytest.mark.usefixtures("driver")
def test_coach_first_name_field_invalid_symbol_validation(driver):
    page = CoachPage(driver)
    page.clear_field(page.coach_first_name_input)
    time.sleep(1)
    page.create_first_name_input(validations["symbol"])
    page.click_create_button()
    page.validation_messages()
    page.clear_field(page.coach_first_name_input)
    time.sleep(1)
    page.create_first_name_input(coach["first_name"])

@pytest.mark.usefixtures("driver")
def test_last_name_field_minimum_length_validation(driver):
    page = CoachPage(driver)
    #firt name validation
    page.clear_field(page.coach_last_name_input)
    time.sleep(1)
    page.create_last_name_input(validations["min_value"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_last_name_field_maximum_length_validation(driver):
    page = CoachPage(driver)
    #validate max value
    page.clear_field(page.coach_last_name_input)
    time.sleep(1)
    page.create_last_name_input(validations["max_value"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_last_name_field_invalid_number_validation(driver):
    page = CoachPage(driver)
    #numeric value
    page.clear_field(page.coach_last_name_input)
    time.sleep(1)
    page.create_last_name_input(validations["Number"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_last_name_field_invalid_symbol_validation(driver):
    page = CoachPage(driver)
    page.clear_field(page.coach_last_name_input)
    time.sleep(1)
    page.create_last_name_input(validations["symbol"])
    page.click_create_button()
    page.validation_messages()
    page.clear_field(page.coach_last_name_input)
    time.sleep(1)
    page.create_last_name_input(coach["last_name"])
    time.sleep(1)

@pytest.mark.usefixtures("driver")
def test_email_field_with_invalid_email_validation(driver):
    page = CoachPage(driver)
    #firt name validation
    page.clear_field(page.email_input)
    time.sleep(1)
    page.create_email_input(validations["invalid_email"])
    page.click_create_button()
    page.validation_messages()

@pytest.mark.usefixtures("driver")
def test_email_field_with_invalid_number_validation(driver):
    page = CoachPage(driver)
    #numeric value
    page.clear_field(page.email_input)
    time.sleep(1)
    page.create_email_input(validations["Number"])
    page.click_create_button()
    page.validation_messages()
    page.clear_field(page.email_input)
    time.sleep(1)
    page.create_email_input(validations["static_email"])
    time.sleep(1)

@pytest.mark.usefixtures("driver")
def test_mobile_number_field_with_less_than_9_numbers_validation(driver):
    page = CoachPage(driver)
    #firt name validation
    page.clear_field(page.mobile_input)
    time.sleep(1)
    page.create_mobile_input(validations["invalid_mobile_less9"])
    page.click_create_button()
    page.validation_messages()

@pytest.mark.usefixtures("driver")
def test_mobile_number_field_with_invalid_text_validation(driver):
    page = CoachPage(driver)
    #validate max value
    page.clear_field(page.mobile_input)
    time.sleep(1)
    page.create_mobile_input(validations["invalid_mobile_text"])
    page.click_create_button()
    page.validation_messages()

@pytest.mark.usefixtures("driver")
def test_mobile_number_field_with_invalid_mobile_with_starting_zero_validation(driver):
    page = CoachPage(driver)
    #numeric value
    page.clear_field(page.mobile_input)
    time.sleep(1)
    page.create_mobile_input(validations["invalid_mobile_zero"])
    page.click_create_button()
    page.validation_messages()
    page.clear_field(page.mobile_input)
    time.sleep(1)
    page.create_mobile_input(coach["mobile"])
    page.click_cancel_button()
    time.sleep(1)

@pytest.mark.usefixtures("driver")
def test_enter_coach_details_for_dob_validation(driver):
    page = CoachPage(driver)
    page.click_coach_tab()
    page.click_on_board_coach_button()
    page.create_first_name_input(coach["first_name"])
    page.create_last_name_input(coach["last_name"])
@pytest.mark.usefixtures("driver")
def test_dob_field_with_age_greater_than_70yrs_validation(driver):
    page = CoachPage(driver)
    #age above 70 yrs
    page.click_and_select_dob(validations["age>70"])
    page.click_select_gender_dropdown()
    page.create_email_input(coach["email"])
    page.create_mobile_input(coach["mobile"])
    page.click_create_button()
    page.validation_messages()
    page.click_cancel_button()
    time.sleep(2)
@pytest.mark.usefixtures("driver")
def test_dob_field_with_age_less_than_18yrs_validation(driver):
    page = CoachPage(driver)
    #age below 5 yrs
    page.click_on_board_coach_button()
    page.create_first_name_input(coach["first_name"])
    page.create_last_name_input(coach["last_name"])
    page.click_and_select_dob(validations["age<5"])
    page.click_select_gender_dropdown()
    page.create_email_input(coach["email"])
    page.create_mobile_input(coach["mobile"])
    page.click_create_button()
    page.validation_messages()
    # page.click_cancel_button()
    