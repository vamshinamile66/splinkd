import pytest
import json
from pages.coach_page import CoachPage

with open("config.json") as f:
    config = json.load(f)
coach = config["coach"]

@pytest.mark.usefixtures("driver")
def test_onboard_coach(driver):
    page = CoachPage(driver)
    page.onboard_coach(
        first_name=coach["first_name"],
        last_name=coach["last_name"],
        dob=coach["dob"],
        gender=coach["gender"],
        email=coach["email"],
        mobile=coach["mobile"]
    )
    