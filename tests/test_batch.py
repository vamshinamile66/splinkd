import pytest
import json
from pages.batch_page import BatchPage

with open("config.json") as f:
    config = json.load(f)
batch_data = config["batch"]

@pytest.mark.usefixtures("driver")
def test_add_batch(driver):
    page = BatchPage(driver)
    page.add_batch(
        program_name=batch_data["program_name"],
        batch_name=batch_data["batch_name"],
        start_hour=batch_data["start_hour"],
        start_minute=batch_data["start_minute"],
        end_hour=batch_data["end_hour"],
        end_minute=batch_data["end_minute"]
    )

@pytest.mark.usefixtures("driver")
def test_batch_mandatory_fields(driver):
    page = BatchPage(driver)
    program_name = "My Test Program"  # Use a valid program name present in your system
    errors = page.check_mandatory_field_errors(program_name)
    print("Mandatory field error messages:")
    for msg in errors:
        print("-", msg)
