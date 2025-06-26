import pytest
import json
from pages.programs_page import ProgramsPage

# Load config values
with open("config.json") as configfile:
    config = json.load(configfile)
program_data = config["program"]

@pytest.mark.usefixtures("driver")
def test_create_program(driver):
    page = ProgramsPage(driver)
    page.create_program(
        title=program_data["title"],
        description=program_data["description"],
        price=program_data["price"],
        sport=program_data["sport"]
    )
    # Optionally, add assertions here to verify program creation

@pytest.mark.usefixtures("driver")
def test_create_program_empty_fields(driver):
    page = ProgramsPage(driver)
    with pytest.raises(Exception) as exc_info:
        page.create_program(
            title="",
            description="",
            price="",
            sport=""
        )
    assert "Please fill out this field" in str(exc_info.value)






