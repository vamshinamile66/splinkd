import pytest
import json
from pages.athletes_page import AthletesPage

with open("config.json") as f:
    config = json.load(f)
athlete = config["athlete"]

@pytest.mark.usefixtures("driver")
def test_onboard_athlete(driver):
    page = AthletesPage(driver)
    page.onboard_athlete(
        first_name=athlete["first_name"],
        last_name=athlete["last_name"],
        dob=athlete["dob"],
        gender=athlete["gender"],
        email=athlete["email"],
        mobile=athlete["mobile"]
    )