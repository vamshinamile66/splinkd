import pytest
import json
import time
from selenium.webdriver.chrome.service import Service
from pages.assign_athletes_to_batch_page import AssignAthletesToBatchPage

with open("config.json") as f:
    config = json.load(f)
program_data = config["program"]
athlete_data=config["athlete"]

@pytest.mark.usefixtures("driver")
def test_click_on_program_tab(driver):
    page = AssignAthletesToBatchPage(driver)
    # Step 1: Click on Programs tab
    page.click_program_tab()

@pytest.mark.usefixtures("driver")
def test_select_and_click_program_name(driver):
    page = AssignAthletesToBatchPage(driver)
    page.select_and_click_program_name(program_data["title"])

@pytest.mark.usefixtures("driver")
def test_click_program_internal_athlete_tab(driver):
    page = AssignAthletesToBatchPage(driver)
    page.click_program_athlete_tab()

@pytest.mark.usefixtures("driver")
def test_click_action_drop_down(driver):
    page = AssignAthletesToBatchPage(driver)
    page.click_actions_dropdown()

@pytest.mark.usefixtures("driver")
def test_click_athlete_onboard_option(driver):
    page = AssignAthletesToBatchPage(driver)
    page.click_athlete_onboard()

@pytest.mark.usefixtures("driver")
def test_search_athlete_select(driver):
    page = AssignAthletesToBatchPage(driver)
    page.click_search_button()
    # page.search_and_select_athlete(athlete_data["first_name"])
    page.search_and_select_athlete("jhon")
    time.sleep(2)  
@pytest.mark.usefixtures("driver")
def test_select_payment_fully_paid(driver):
    page = AssignAthletesToBatchPage(driver)
    page.select_payment_status_via_keys("Fully Paid")

@pytest.mark.usefixtures("driver")
def test_click_add_athlete_submit_button(driver):
    page = AssignAthletesToBatchPage(driver)
    page.click_add_athlete_submit()
    # Step 8: Verify success message with retry wait
    success_message = page.get_success_message_text()
    print(f"[INFO] Success message: {success_message}")
    assert "athlete added to batch successfully" in success_message.lower(), \
        f"Expected success message not found. Got: {success_message}"

