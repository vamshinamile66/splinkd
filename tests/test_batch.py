import pytest
import json
import time
from pages.batch_page import BatchPage

with open("config.json") as f:
    config = json.load(f)
batch_data = config["batch"]
batch_validations = config["batch_validations"]
program_data = config["program"]


@pytest.mark.usefixtures("driver")
def test_click_on_program_tab_and_navigate_to_program_detailed_view(driver):
    page = BatchPage(driver)
    page.click_program_tab()
    page.select_and_click_program_name(program_data["title"])
    time.sleep(1)
@pytest.mark.usefixtures("driver")
def test_click_on_add_batch_button(driver):
    page = BatchPage(driver)
    page.click_add_batch_button()
    time.sleep(1)
@pytest.mark.usefixtures("driver")
def test_mandatory_field_validation_errors(driver):
    page = BatchPage(driver)
    page.click_save_button()
    page.validation_messages()
    time.sleep(1)
    page.click_cancel_button()
@pytest.mark.usefixtures("driver")
def test_click_add_batch_buttons(driver):
    page = BatchPage(driver)
    page.click_add_batch_button()
    time.sleep(1)
@pytest.mark.usefixtures("driver")
def test_enter_batch_details(driver):
    page = BatchPage(driver)
    time.sleep(1)
    page.create_batch_name(batch_data["batch_name"])
    page.select_start_time(batch_data["start_time"])
    page.select_end_time(batch_data["end_time"])
    time.sleep(1)
@pytest.mark.usefixtures("driver")
#validation for batch title field
def test_batch_title_field_minimum_length_validation(driver):
    page = BatchPage(driver)
    page.clear_field(page.batch_name_input)
    time.sleep(1)
    page.create_batch_name(batch_validations["min_value"])
    page.select_start_time(batch_data["start_time"])
    page.select_end_time(batch_data["end_time"])
    page.click_save_button()
    page.validation_messages()
def test_batch_title_field_maximum_length_validation(driver):
    page = BatchPage(driver)
    page.clear_field(page.batch_name_input)
    time.sleep(1)
    page.create_batch_name(batch_validations["max_value"])
    page.click_save_button()
    page.validation_messages()
    time.sleep(1)
def test_batch_title_field_invalid_number_validation(driver):
    page = BatchPage(driver)
    page.clear_field(page.batch_name_input)
    time.sleep(1)
    page.create_batch_name(batch_validations["Number"])
    page.click_save_button()
    page.validation_messages()
    time.sleep(1)
def test_batch_title_field_invalid_symbols_validation(driver):
    page = BatchPage(driver)
    page.clear_field(page.batch_name_input)
    time.sleep(1)
    page.create_batch_name(batch_validations["symbols"])
    page.click_save_button()
    page.validation_messages()
    time.sleep(1)
def test_batch_title_enter_valid_text_validation(driver):
    page = BatchPage(driver)
    page.clear_field(page.batch_name_input)
    time.sleep(1)
    page.create_batch_name(program_data["title"])
    time.sleep(1)
  
@pytest.mark.usefixtures("driver")
#validation for time field
def test_invalid_time_by_keeping_end_time_befor_start_time(driver):
    page = BatchPage(driver)
    page.select_start_time(batch_data["end_time"])
    page.select_end_time(batch_data["start_time"])
    page.click_save_button()
    time.sleep(2)
    page.validation_messages()
    time.sleep(1)
    page.click_cancel_button()

@pytest.mark.usefixtures("driver")
def test_add_batch(driver):
    page = BatchPage(driver)
    page.click_add_batch_button()
    time.sleep(2)
    page.create_batch_name(batch_data["batch_name"])
    page.select_start_time(batch_data["start_time"])
    page.select_end_time(batch_data["end_time"])
    page.click_save_button()
    time.sleep(2)
    page.check_toast_message()




