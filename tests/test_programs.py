import pytest
import json
import time
from pages.programs_page import ProgramsPage

# Load config values
with open("config.json") as configfile:
    config = json.load(configfile)
program_data = config["program"]
validations = config["validations"]

# @pytest.mark.usefixtures("driver")
# def test_mandatory_field_validation_errors(driver):
#     page = ProgramsPage(driver)
#     page.click_programs_tab()
#     page.click_create_new_program_button()
#     page.click_next_button()  # Attempt to proceed without filling fields
#     page.validation_messages()
#     time.sleep(2)

# @pytest.mark.usefixtures("driver")
# #validation for program title field
# def test_Enter_program_details_in_field(driver):
#     page = ProgramsPage(driver)
#     page.click_programs_tab()  
#     page.click_create_new_program_button()
#     page.create_program_title(program_data["title"])
#     page.create_program_desc(program_data["description"])
#     page.create_program_price(program_data["price"])
#     page.select_sports_dropdown()
#     page.select_bestfit_level()
# def test_program_title_field_minimum_length_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_title_input)
#     time.sleep(1)
#     page.create_program_title(validations["min_value"])
#     page.click_next_button()  
#     page.validation_messages()
#     time.sleep(1)
#     page.clear_field(page.program_title_input)
#     time.sleep(1)
# def test_program_title_field_maximum_length_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_title_input)
#     time.sleep(1)
#     page.create_program_title(validations["max_value"])
#     page.click_next_button()
#     page.validation_messages()
#     time.sleep(1)
# def test_program_title_field_invalid_number_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_title_input)
#     time.sleep(1)
#     page.create_program_title(validations["Number"])
#     page.click_next_button()
#     page.validation_messages()
#     time.sleep(2)
# def test_program_title_field_invalid_symbol_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_title_input)
#     time.sleep(1)
#     page.create_program_title(validations["symbol"])
#     page.click_next_button()
#     page.validation_messages()
#     time.sleep(2)
    
# @pytest.mark.usefixtures("driver")
# #validation for program description field
# def test_enter_title_in_field(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_title_input)
#     page.create_program_title( program_data["title"])
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_description_field_minimum_length_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_desc_input)
#     page.create_program_desc(validations["min_value"])
#     page.click_next_button()  
#     page.validation_messages()
#     time.sleep(1)
# @pytest.mark.usefixtures("driver")
# def test_description_field_maximum_length_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_desc_input)
#     time.sleep(1)
#     page.create_program_desc(validations["max_program_value"])
#     page.click_next_button()
#     page.validation_messages()
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_enter_program_description_in_field(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_desc_input)
#     page.create_program_desc( program_data["description"])

# def test_price_field_minimum_length_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_price_input)
#     time.sleep(1)
#     page.create_program_price(validations["price_min"])
#     page.click_next_button()
#     page.validation_messages()
#     time.sleep(1)

# def test_price_field_maximum_length_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_price_input)
#     time.sleep(1)    
#     page.create_program_price(validations["price_max"])
#     page.click_next_button()
#     page.validation_messages()
#     time.sleep(1)

# def test_price_field_alpha_text_validation(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_price_input)
#     time.sleep(1)
#     page.create_program_price(validations["alphabit"])
#     page.click_next_button()
#     page.validation_messages()
#     time.sleep(1)

# def test_enter_program_price_in_field(driver):
#     page = ProgramsPage(driver)
#     page.clear_field(page.program_price_input)
#     time.sleep(1)
#     page.create_program_price(program_data["price"])
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_click_on_next_button_screen(driver):
#     page = ProgramsPage(driver)
#     page.click_next_button()
#     time.sleep(2)

# @pytest.mark.usefixtures("driver")
# #validation for program cover image more than 5 mb
# def test_validate_cover_image_by_uploading_large_file_more_than_5mb(driver):
#     page = ProgramsPage(driver)
#     page.upload_cover_image_and_create("C:/Users/vamshi.namile/Desktop/Test data Upload/File size greater 5/largefile.gif")
#     page.toast_message("File size")
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# #validation for program cover image more than 5 mb
# def test_validate_cover_image_by_uploading_invalid_file_excel(driver):
#     page = ProgramsPage(driver)
#     page.upload_cover_image_and_create("C:/Users/vamshi.namile/Desktop/Test data Upload/splinktestdata/file1.xlsx")
#     page.toast_message("error")
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_click_cancel_button(driver):
#     page = ProgramsPage(driver)
#     page.click_cancel_button()
#     time.sleep(2)

# @pytest.mark.usefixtures("driver")
# def test_click_on_program_tab(driver):
#     page = ProgramsPage(driver)
#     page.click_programs_tab()  
# @pytest.mark.usefixtures("driver")
# def test_click_on_create_new_program_button(driver):
#     page = ProgramsPage(driver)
#     page.click_programs_tab()
#     page.click_create_new_program_button()
# @pytest.mark.usefixtures("driver")
# def test_enter_program_details(driver):
#     page = ProgramsPage(driver)
#     page.create_program_title(program_data["title"])
#     page.create_program_desc(program_data["description"])
#     page.create_program_price(program_data["price"])
#     page.select_sports_dropdown()
#     page.select_bestfit_level()

# @pytest.mark.usefixtures("driver")
# def test_click_on_next_button(driver):
#     page = ProgramsPage(driver)
#     page.click_next_button()

# @pytest.mark.usefixtures("driver")
# def test_upload_image(driver):
#     page = ProgramsPage(driver)
#     page.upload_cover_image_and_create(program_data["cover_image_path"])

# @pytest.mark.usefixtures("driver")
# def test_click_on_submit_program_button(driver):
#     page = ProgramsPage(driver)
#     page.click_program_submit_button()
#     page.is_success_message_displayed()

# @pytest.mark.usefixtures("driver")
# def test_search_program_by_title(driver):
#     time.sleep(5)
#     page = ProgramsPage(driver)
#     page.search_program(program_data["title"])
#     time.sleep(2)

# @pytest.mark.usefixtures("driver")
# def test_click_on_program_name(driver):
#     page = ProgramsPage(driver)
#     page.click_program_by_name(program_data["title"])
#     time.sleep(2)

# @pytest.mark.usefixtures("driver")
# def test_verify_program_details(driver):
#     page = ProgramsPage(driver)
#      # 1. Assert Title
#     actual_title = page.get_program_title().strip().lower()
#     assert actual_title == program_data["title"].strip().lower(), f"❌ Expected title '{program_data['title']}', got '{actual_title}'"
#     print(f"✅ Program title is correct: {actual_title}")


#50 programs
import pytest
import string
import time
from pages.programs_page import ProgramsPage

# 🔹 Generate 50 program datasets with unique names
def generate_programs():
    programs = []
    for i, letter in enumerate(string.ascii_uppercase[:50], start=1):
        timestamp = int(time.time())  # ensures uniqueness on reruns
        programs.append({
            "title": f"Program {letter}",
            "description": f"Auto-generated description for Program {letter}",
            "price": str(100 + i),
            "cover_image_path": "test_data/images/sample.png"
        })
    return programs

programs = generate_programs()

# 🔹 End-to-end test: creates a program
@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("program_data", programs)
def test_create_program(driver, program_data):
    page = ProgramsPage(driver)

    # Step 1: Navigate & click "Create Program"
    page.click_programs_tab()
    time.sleep(2)
    page.click_create_new_program_button()
    time.sleep(2)
    # Step 2: Enter program details
    page.clear_field(page.program_title_input)
    time.sleep(1)
    page.create_program_title(program_data["title"])
    time.sleep(1)
    page.clear_field(page.program_desc_input)
    time.sleep(1)
    page.create_program_desc(program_data["description"])
    time.sleep(1)
    page.clear_field(page.program_price_input)
    time.sleep(1)
    page.create_program_price(program_data["price"])
    page.select_sports_dropdown()
    page.select_bestfit_level()
    # Step 3: Go next
    page.click_next_button()
    # Step 4: Upload cover image
    page.upload_cover_image_and_create(program_data["cover_image_path"])
    # Step 5: Submit program
    page.click_program_submit_button()
    # Step 6: Verify success
    assert page.is_success_message_displayed()
