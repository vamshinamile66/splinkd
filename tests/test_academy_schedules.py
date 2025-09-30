
import pytest
import json
from datetime import datetime
from pages.academy_schedules_page import SchedulesPage

# Load config values
with open("config.json") as configfile:
    config = json.load(configfile)
program_data = config["program"]
#today date
today = datetime.today()
today_date = today.strftime("%B %d, %Y")


@pytest.mark.usefixtures("driver")
def test_click_on_schedules_tab(driver):
    page = SchedulesPage(driver)
    page.click_schedules_tab()

@pytest.mark.usefixtures("driver")
def test_Is_schedules_by_view_options_displayed(driver):
    page = SchedulesPage(driver)
    page.verify_view_options_displayed()

@pytest.mark.usefixtures("driver")
def test_check_Is_created_program_is_displayed(driver):
    page = SchedulesPage(driver)
    program, coach = page.find_program_and_coach( title=program_data["title"])
    if program:
        print("✅ program found and details:")
        print(f"Program: {program}")
        print(f"👨‍🏫{coach}")
    else:
        print("❌ Summer program not found")