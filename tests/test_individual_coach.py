  
import json
import time
import pytest
from pages.individual_coach_page import SignupPage

#load configuration from config.json file
with open("config.json") as config_file:
    config=json.load(config_file)


# def test_signup_function(driver):
#     driver.get(config["base_url"])
#     # Generate a unique email to avoid conflicts
#     # timestamp = int(time.time())
#     # username = f"qa{timestamp}@otsi.co.in"
#     #data from config file
#     email = config["coach"]["email"]
#     newpassword = config["coach"]["password"]
#     confirm_password = config["coach"]["confirm_password"]
#     program_name = config["program"]["title"]
#     athlete_name = config["athlete"]["first_name"]
#     captch_url= config["captch_url"]


    #temporary comment & need to uncomment later (remove login)
    # # Initialize signup page and perform signup
    # signup=SignupPage(driver)
    # signup.signup(email,newpassword,confirm_password,captch_url)

@pytest.mark.usefixtures("driver")
def test_login_correct_username_correct_password(driver):
    """Test login with correct username and correct password."""
    driver.get(config["base_url"])
    athlete_name = f"{config['athlete']['first_name']} {config['athlete']['last_name']}"
    program_name = config["program"]["title"]
    username = config["coach"]["email"]
    password = config["coach"]["password"]
    
    signup = SignupPage(driver)
    signup.login(username, password)

    time.sleep(4)

    #click on programs tab
    signup.click_programs_tab()
    # Mark attendance for the specified program and athlete
    signup.test_mark_attendance(program_name, athlete_name)
    # logout after test completion
    signup.logout()
