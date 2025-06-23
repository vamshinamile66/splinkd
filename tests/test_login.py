import json
import pytest
import time
from pages.login_page import LoginPage

# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

@pytest.mark.usefixtures("driver")
def test_login_correct_username_correct_password(driver):
    """Test login with correct username and correct password."""
    driver.get(config["base_url"])
    
    username = config["username"]
    password = config["password"]
    
    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(2)

    if login_page.is_logged_in():
        print("Login test with correct username and correct password executed successfully!")
        login_page.signout()
        driver.get(config["base_url"])
    else:
        assert False, "Login failed with correct username and correct password"


@pytest.mark.usefixtures("driver")
def test_login_correct_username_incorrect_password(driver):
    """Test login with correct username and incorrect password."""
    driver.get(config["base_url"])
    time.sleep(2)
    username = config["username"]
    password = "wrongpassword"
    
    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(2)

    assert not login_page.is_logged_in(), "Login succeeded with correct username and incorrect password"
    print("Login test with correct username and incorrect password executed successfully!")

@pytest.mark.usefixtures("driver")
def test_login_incorrect_username_correct_password(driver):
    """Test login with incorrect username and correct password."""
    driver.get(config["base_url"])
    time.sleep(5)
    username = "invalid_user"
    password = config["password"]
    
    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(2)

    assert not login_page.is_logged_in(), "Login succeeded with incorrect username and correct password"
    print("Login test with incorrect username and correct password executed successfully!")

@pytest.mark.usefixtures("driver")
def test_login_empty_username_empty_password(driver):
    """Test login with empty username and empty password."""
    driver.get(config["base_url"])
    
    username = ""
    password = ""
    
    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(2)

    assert not login_page.is_logged_in(), "Login succeeded with empty username and empty password"
    print("Login test with empty username and empty password executed successfully!")

