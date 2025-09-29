import pytest
import json
import logging
from pages.assign_coach_to_batch_page import AssignCoachToBatchPage

logger = logging.getLogger(__name__)

with open("config.json") as f:
    config = json.load(f)
program_data = config["program"]


@pytest.mark.usefixtures("driver")
def test_click_on_program_tab(driver):
    page = AssignCoachToBatchPage(driver)
    page.click_program_tab()

@pytest.mark.usefixtures("driver")
def test_select_and_click_on_program_name(driver):
    page = AssignCoachToBatchPage(driver)
    page.select_and_click_program_name(program_data["title"])
  
@pytest.mark.usefixtures("driver")
def test_click_on_add_coach_button(driver):
    page = AssignCoachToBatchPage(driver)
    page.click_add_coach_button()

@pytest.mark.usefixtures("driver")
def test_select_coach_in_the_list(driver):
    page = AssignCoachToBatchPage(driver)   
    page.click_coach_by_name("Jane Smith")

@pytest.mark.usefixtures("driver")
def test_confirm_add_coach_to_batch(driver):
    page = AssignCoachToBatchPage(driver)    
    page.click_confirm_add_coach()
    # Step 5: Verify success message
    success_message = page.get_success_message_text()
    assert "coach added to batch successfully" in success_message.lower(), \
        f"Expected success message not found. Got: {success_message}"

