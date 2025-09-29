 
  
import json
import time
import pytest
from pages.individual_athlete_page import SignupPage

#load configuration from config.json file
with open("config.json") as config_file:
    config=json.load(config_file)


def test_signup_function(driver):
    driver.get(config["base_url"])
 
    # Generate a unique email to avoid conflicts
    # timestamp = int(time.time())
    # username = f"qa{timestamp}@otsi.co.in"
    # email = config["athlete"]["email"]
    # newpassword = config["athlete"]["password"]
    # confirm_password = config["athlete"]["confirm_password"]
    program_name = config["program"]["title"]
    # captch_url= config["captch_url"]
    #enble after login removed
    # # Initialize signup page and perform signup
    signup=SignupPage(driver)
    # signup.signup(email,newpassword,confirm_password,captch_url)
    # time.sleep(5)
    username= config["athlete"]["email"]
    password= config["athlete"]["password"]
    #remove login later
    # logout after test completion
    signup.login(username, password)
    time.sleep(5)
    # Click on Programs tab
    signup.click_programs_tab()
    time.sleep(5)
    # Verify attendance for the specified program
    signup.verify_attendance(program_name)
