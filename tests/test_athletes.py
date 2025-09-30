import pytest
import json
import time
from pages.athletes_page import AthletesPage

with open("config.json") as f:
    config = json.load(f)
athlete = config["athlete"]
validations = config["validations"]


# email-Replace placeholder with dynamic value
timestamp = int(time.time())
dynamic_email = f"athlete{timestamp}@otsi.co.in"
athlete['email'] = dynamic_email

#------onboard athlete test cases------#

@pytest.mark.usefixtures("driver")
def test_click_on_athlete_tab_and_navigation_to_athlete_screen(driver):
    page = AthletesPage(driver)
    page.click_athlete_tab()

@pytest.mark.usefixtures("driver")
def test_click_on_actions_dropdown_and_select_select_add_athlete(driver):
    page = AthletesPage(driver)
    page.click_actions_dropdown()
    page.click_athlete_onboard()

@pytest.mark.usefixtures("driver")
def test_enter_athlete_details(driver):
    page = AthletesPage(driver)
    page.create_first_name(athlete["first_name"])
    page.create_last_name(athlete["last_name"])
    page.click_and_select_dob(athlete["year"])
    page.click_and_select_gender()
    page.create_email(athlete["email"])
    page.create_mobile(athlete["mobile"])

@pytest.mark.usefixtures("driver")
def test_click_submit_athlete_details_button(driver):
    page = AthletesPage(driver)
    page.click_create_button()
    page.toast_message("Successful")
#------------------------------------------#
@pytest.mark.usefixtures("driver")
def test_existing_email_validation_error(driver):
    page = AthletesPage(driver)
    time.sleep(2)
    page.click_actions_dropdown()
    page.click_athlete_onboard()
    page.create_first_name(athlete["first_name"])
    page.create_last_name(athlete["last_name"])
    page.click_and_select_dob(athlete["year"])
    page.click_and_select_gender()
    page.create_email(athlete["email"])
    page.create_mobile(athlete["mobile"])
    page.click_create_button()
    page.toast_message("already exists")
    page.click_cancel_button()

@pytest.mark.usefixtures("driver")
def test_mandatory_field_validation_errors(driver):
    page = AthletesPage(driver)
    page.click_athlete_tab()
    page.click_actions_dropdown()
    page.click_athlete_onboard()
    page.click_create_button()
    page.validation_messages()
    page.click_cancel_button()

@pytest.mark.usefixtures("driver")
def test_entered_athlete_details_for_name_validation(driver):
    page = AthletesPage(driver)
    page.click_athlete_tab()
    page.click_actions_dropdown()
    page.click_athlete_onboard()
    page.create_first_name(athlete["first_name"])
    page.create_last_name(athlete["last_name"])
    page.click_and_select_dob(athlete["year"])
    page.click_and_select_gender()
    page.create_email(validations["static_email"])
    page.create_mobile(athlete["mobile"])

@pytest.mark.usefixtures("driver")
def test_athlete_first_name_field_minimum_length_validation(driver):
    page = AthletesPage(driver)
    #firt name validation
    page.clear_field(page.first_name_input)
    time.sleep(1)
    page.create_first_name(validations["min_value"])
    page.click_create_button()
    page.validation_messages()

@pytest.mark.usefixtures("driver")
def test_athlete_first_name_field_maximum_length_validation(driver):
    page = AthletesPage(driver)
    #validate max value
    page.clear_field(page.first_name_input)
    time.sleep(1)
    page.create_first_name(validations["max_value"])
    page.click_create_button()
    time.sleep(2)
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_athlete_first_name_field_invalid_number_validation(driver):
    page = AthletesPage(driver)
    #numeric value
    page.clear_field(page.first_name_input)
    time.sleep(1)
    page.create_first_name(validations["Number"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_athlete_first_name_field_invalid_symbol_validation(driver):
    page = AthletesPage(driver)
    #numeric value
    page.clear_field(page.first_name_input)
    time.sleep(1)
    page.create_first_name(validations["symbol"])
    page.click_create_button()
    page.validation_messages()
    page.clear_field(page.first_name_input)
    time.sleep(1)
    page.create_first_name(athlete["first_name"])

@pytest.mark.usefixtures("driver")
def test_athlete_last_name_field_minimum_length_validation(driver):
    page = AthletesPage(driver)
    page.clear_field(page.last_name_input)
    time.sleep(1)
    page.create_last_name(validations["min_value"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_athlete_last_name_field_maximum_length_validation(driver):
    page = AthletesPage(driver)
    #validate max value
    page.clear_field(page.last_name_input)
    time.sleep(1)
    page.create_last_name(validations["max_value"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_athlete_last_name_field_invalid_number_validation(driver):
    page = AthletesPage(driver)
    #numeric value
    page.clear_field(page.last_name_input)
    time.sleep(1)
    page.create_last_name(validations["Number"])
    page.click_create_button()
    page.validation_messages()

@pytest.mark.usefixtures("driver")
def test_athlete_last_name_field_invalid_symbol_validation(driver):
    page = AthletesPage(driver)
    #numeric value
    page.clear_field(page.last_name_input)
    time.sleep(1)
    page.create_last_name(validations["symbol"])
    page.click_create_button()
    page.validation_messages()
    page.clear_field(page.last_name_input)
    time.sleep(1)
    page.create_last_name(athlete["last_name"])
    time.sleep(1)

@pytest.mark.usefixtures("driver")
def test_email_field_invalid_email_validation(driver):
    page = AthletesPage(driver)
    #firt name validation
    page.clear_field(page.email_input)
    time.sleep(1)
    page.create_email(validations["invalid_email"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_email_field_invalid_number_validation(driver):
    page = AthletesPage(driver)
    #numeric value
    page.clear_field(page.email_input)
    time.sleep(1)
    page.create_email(validations["Number"])
    page.click_create_button()
    page.validation_messages()
    page.clear_field(page.email_input)
    time.sleep(1)
    page.create_email(validations["static_email"])
    time.sleep(1)

@pytest.mark.usefixtures("driver")
def test_mobile_number_field_minimum_length_validation(driver):
    page = AthletesPage(driver)
    #firt name validation
    page.clear_field(page.mobile_input)
    time.sleep(1)
    page.create_mobile(validations["invalid_mobile_less9"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_mobile_number_field_invalid_text_validation(driver):
    page = AthletesPage(driver)
    #validate max value
    page.clear_field(page.mobile_input)
    time.sleep(1)
    page.create_mobile(validations["invalid_mobile_text"])
    page.click_create_button()
    page.validation_messages()
@pytest.mark.usefixtures("driver")
def test_mobile_number_field_invalid_mobile_starts_with_zero_validation(driver):
    page = AthletesPage(driver)
    #numeric value
    page.clear_field(page.mobile_input)
    time.sleep(1)
    page.create_mobile(validations["invalid_mobile_zero"])
    page.click_create_button()
    page.validation_messages()
    page.clear_field(page.mobile_input)
    time.sleep(1)
    page.create_mobile(athlete["mobile"])
    page.click_cancel_button()
    time.sleep(1)


@pytest.mark.usefixtures("driver")
def test_enter_athlete_details_for_dob_validation(driver):
    page = AthletesPage(driver)
    page.click_actions_dropdown()
    page.click_athlete_onboard()
    page.create_first_name(athlete["first_name"])
    page.create_last_name(athlete["last_name"])
@pytest.mark.usefixtures("driver")
def test_dob_field_with_age_greater_than_70_validation(driver):
    page = AthletesPage(driver)
    #age above 70 yrs
    page.click_and_select_dob(validations["age>70"])
    page.click_and_select_gender()
    page.create_email(validations["static_email"])
    page.create_mobile(athlete["mobile"])
    page.click_create_button()
    page.validation_messages()
    page.click_cancel_button()
    time.sleep(2)
@pytest.mark.usefixtures("driver")
def test_dob_field_with_age_less_than_5_validation(driver):
    page = AthletesPage(driver)
    #age below 5 yrs
    page.click_actions_dropdown()
    page.click_athlete_onboard()
    page.create_first_name(athlete["first_name"])
    page.create_last_name(athlete["last_name"])
    page.click_and_select_dob(validations["age<5"])
    time.sleep(1)
    page.check_parent_guardian_heading_displayed()
    page.click_cancel_button()



    


    


