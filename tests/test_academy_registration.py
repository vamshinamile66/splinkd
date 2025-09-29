import json
import time
import pytest
from pages.academy_registration_page import RegisterAcademyPage
import pytest
import os
import time

#load configuration from config.json file
with open("config.json") as config_file:
    config=json.load(config_file)
    validations = config["validations"]

@pytest.mark.usefixtures("driver")
def test_signup_for_academy_registration(driver):
    driver.get(config["base_url"])
    academypage=RegisterAcademyPage(driver)
    # Generate a unique email to avoid conflicts
    captch_url= config["captch_url"]
    timestamp = int(time.time())
    username = f"qa{timestamp}@otsi.co.in"
    newpassword = config["signup"]["newpassword"]
    confirm_password = config["signup"]["confirmpassword"] 
    # Initialize signup page and perform signup
    academypage.signup(username,newpassword,confirm_password,captch_url)
    time.sleep(2)


@pytest.mark.usefixtures("driver")
def test_mandate_field_validation_in_first_page_errors(driver):
        academypage = RegisterAcademyPage(driver)
        academy = config["academy_reg"]
        print("Academy registration started without filling any data")
        academypage.next_button_click()
        time.sleep(1)
        # Capture actual errors
        errors = academypage.validation_academy_registration()
        # Load expected from config.json
        expected_fields = config["academy_required_fields"]["expected"]

        print("Expected Errors:", expected_fields)
        print("Actual Errors:", errors)
        # Check that every expected field has a Required error
        for field in expected_fields:
            assert field in errors, f"Missing error for: {field}"
            assert "required" in errors[field], f"Incorrect error for {field}: {errors[field]}"
           
        # Check no extra unexpected errors
        unexpected = [f for f in errors if f not in expected_fields]
        assert not unexpected, f"Unexpected errors found: {unexpected}"

#enter details in first page and click next then check for second page
@pytest.mark.usefixtures("driver")
def test_mandate_field_validation_in_second_page_errors(driver):
        academypage = RegisterAcademyPage(driver)
        academy = config["academy_reg"]
        # ---------- Test 2: Location empty validation ----------
        print("Checking location field validations by entering remaining details")
        academypage.academy_name_field(academy["academy_name"])
        academypage.mobile_number_field(academy["mobile_number"])
        academypage.select_sports(academy["sports"])
        academypage.upload_logo(academy["logo_path"])
        academypage.upload_file(academy["file_path"])
        academypage.next_button_click()
        time.sleep(1)
        academypage.search_and_select_location("")  # Leave location empty
        academypage.click_create_profile()
        print("clicked on the create button without adding location")
        time.sleep(1)
        assert academypage.is_branch_error_displayed(), "Branch error message not displayed when location is empty"
        print("Branch error message: At least one branch location is required")
        academypage.click_previous()
        time.sleep(2)

@pytest.mark.usefixtures("driver")
def test_academy_name_field_minimum_length_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academypage.clear_field(academypage.academy_name_input)
        time.sleep(1)
        #Entered minimum characters
        academypage.academy_name_field(validations["min_value"])  # Less than 3 characters
        academypage.next_button_click()
        academypage.validation_academy_registration()
@pytest.mark.usefixtures("driver")
def test_academy_name_field_maximum_length_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academy = config["academy_reg"]
        #max charecters
        academypage.clear_field(academypage.academy_name_input)
        time.sleep(1)
        academypage.academy_name_field(validations["max_value"])
        academypage.next_button_click()
        academypage.validation_academy_registration()
@pytest.mark.usefixtures("driver")
def test_academy_name_field_invalid_number__validations(driver):
        academypage = RegisterAcademyPage(driver)
        #invalid input
        academypage.clear_field(academypage.academy_name_input)
        time.sleep(1)
        academypage.academy_name_field(validations["Number"])
        academypage.next_button_click()
        academypage.validation_academy_registration()
        academypage.clear_field(academypage.academy_name_input)
        time.sleep(1)
@pytest.mark.usefixtures("driver")
def test_academy_name_field_invalid_symbol__validations(driver):
        academypage = RegisterAcademyPage(driver)
        academy = config["academy_reg"]
        #invalid input
        academypage.clear_field(academypage.academy_name_input)
        time.sleep(1)
        academypage.academy_name_field(validations["symbol"])
        academypage.next_button_click()
        academypage.validation_academy_registration()
        academypage.clear_field(academypage.academy_name_input)
        time.sleep(1)
        academypage.academy_name_field(academy["academy_name"])
@pytest.mark.usefixtures("driver")
def test_logo_upload_image_greater_than_5mb_validations(driver):
        academypage = RegisterAcademyPage(driver)
        time.sleep(1)
        #trying to upload more than 5 mb
        academypage.upload_logo("C:/Users/vamshi.namile/Desktop/Test data Upload/File size greater 5/largefile.gif")  # File larger than 5MB
        academypage.toast_message("File size")
        time.sleep(1)  
@pytest.mark.usefixtures("driver")
def test_logo_upload_Invalid_image_excel_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academypage.upload_logo("C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/TestDataSplink_table.xlsx")  #invalid excel file
        academypage.toast_message("error")
        time.sleep(1)
@pytest.mark.usefixtures("driver")
def test_logo_upload_valid_image_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academypage.upload_logo("C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/academy2.jpeg")  #normal file
        time.sleep(1)
        print("✅ Academy Logo uploaded successfully")

@pytest.mark.usefixtures("driver")
def test_mobile_field_with_less_than_10__digits_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academypage.clear_field(academypage.mobile_number_input)
        time.sleep(1)
        #Entered minimum characters
        academypage.mobile_number_field(validations["invalid_mobile_less9"])  # Less than 3 characters
        academypage.next_button_click()
        academypage.validation_academy_registration()
@pytest.mark.usefixtures("driver")
def test_mobile_field_with_invalid_text_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academy = config["academy_reg"]
        academypage.clear_field(academypage.mobile_number_input)
        time.sleep(1)
        academypage.mobile_number_field(validations["invalid_mobile_text"])
        academypage.next_button_click()
        academypage.validation_academy_registration()
@pytest.mark.usefixtures("driver")
def test_mobile_field_with_invalid_symbol_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academypage.clear_field(academypage.mobile_number_input)
        time.sleep(1)
        academypage.mobile_number_field(validations["mobile_symbols"])
        academypage.next_button_click()
        academypage.validation_academy_registration()
@pytest.mark.usefixtures("driver")
def test_mobile_field_with_invalid_zero_starting_number_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academy = config["academy_reg"]
        #invalid input
        academypage.clear_field(academypage.mobile_number_input)
        time.sleep(1)
        academypage.mobile_number_field(validations["invalid_mobile_zero"])
        academypage.next_button_click()
        academypage.validation_academy_registration()
        academypage.clear_field(academypage.mobile_number_input)
        time.sleep(1)
        academypage.mobile_number_field(academy["mobile_number"])
        
@pytest.mark.usefixtures("driver")
def test_upload_file_with_file_size_more_than_5mb_validations(driver):
        academypage = RegisterAcademyPage(driver)
        time.sleep(1)
        #trying to upload more than 5 mb
        academypage.upload_file("C:/Users/vamshi.namile/Desktop/Test data Upload/File size greater 5/Issues-Meenestham above5.docx")  # File larger than 5MB
        academypage.toast_message("File size")
        time.sleep(1)

@pytest.mark.usefixtures("driver")
def test_upload_file_delete_existing_file_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academypage.delete_file("TestDataSplink_table.xlsx")

@pytest.mark.usefixtures("driver")
def test_upload_specific_files(driver):
        academypage = RegisterAcademyPage(driver)
        academypage.upload_files(
        r"C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/cricketq.jpg",
        r"C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/basket.jpg",
        r"C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/file1.xlsx",
        r"C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/file2.xlsx",
        r"C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/file3.xlsx")
        time.sleep(1)
        choose_available = academypage.is_choose_file_option_available()
        print(f"👉 After 5 uploads, 'Choose File' available? {choose_available}")
        assert not choose_available, "'Choose File' should be hidden/disabled after 5 uploads"

@pytest.mark.usefixtures("driver")
def test_upload_delete_5th_file_and_check__is_choose_option_displayed_validate(driver):
    academypage = RegisterAcademyPage(driver)
    # Step 3: Delete 1 file (say file3.xlsx)
    academypage.delete_file("file1.xlsx")
    # Step 4: Check if Choose File option is visible again
    choose_available_after_delete = academypage.is_choose_file_option_available()
    print(f"👉 After deleting one file, 'Choose File' available? {choose_available_after_delete}")

@pytest.mark.usefixtures("driver")
def test_upload_file_with_valid_file_validations(driver):
        academypage = RegisterAcademyPage(driver)
        academypage.upload_file("C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/50splink.xlsx")  # File larger than 5MB
        print("✅ Academy Supporting document uploaded successfully")

@pytest.mark.usefixtures("driver")
def test_click_next_button(driver):
    academypage = RegisterAcademyPage(driver)
    academypage.next_button_click()
@pytest.mark.usefixtures("driver")
def test_search_and_select_location(driver):
    academy = config["academy_reg"]
    academypage = RegisterAcademyPage(driver)
    academypage.search_and_select_location(academy["location"])
@pytest.mark.usefixtures("driver")
def test_click_create_profile_button_capture_message(driver):
    academypage = RegisterAcademyPage(driver)
    academypage.click_create_profile()
    academypage.toast_message("Academy Profile")
    time.sleep(3)
@pytest.mark.usefixtures("driver")
def test_click_signout_button(driver):
    academypage = RegisterAcademyPage(driver)
    academypage.logout()
    time.sleep(1)