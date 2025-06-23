import json
from time import time
import pytest
from pages.signup_page import SignupPage

#load configuration from config.json file
with open("config.json") as config_file:
    config=json.load(config_file)



def test_signup_function(driver):
    driver.get(config["base_url"])
    #get credentials
    username = config["signup"]["email"]
    newpassword = config["signup"]["newpassword"]
    confirm_password = config["signup"]["confirmpassword"]
    
   
    # Initialize signup page and perform signup
    signup=SignupPage(driver)
    signup.signup(username,newpassword,confirm_password)


