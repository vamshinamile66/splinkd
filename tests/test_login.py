import json
import pytest
import time
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    time.sleep(1)

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
    time.sleep(1)
    username = config["username"]
    password = "wrongpassword"
    
    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(1)

    assert not login_page.is_logged_in(),"Login succeeded with correct username and incorrect password"
    # Wait for the toast message to appear and extract it
    from selenium.common.exceptions import TimeoutException
    wait = WebDriverWait(driver, 10)

    try:
        # Wait for presence of the error message element (same selector as other test)
        error_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p[data-slot="form-message"]'))
        )
        WebDriverWait(driver, 5).until(lambda d: error_element.is_displayed())
        actual_error_message = error_element.text.strip()
    except TimeoutException:
        actual_error_message = ""
        print("❌ Error message not found within timeout.")
        print("actual error message:", actual_error_message)
    expected_invalid_password_error_message = config["expected_invalid_password_error_message"]
    print(f"Expected error message: '{expected_invalid_password_error_message}'")
    print("Captured error message:", actual_error_message)
    assert actual_error_message == expected_invalid_password_error_message
    print("Login test with correct username and incorrect password executed successfully!")

@pytest.mark.usefixtures("driver")
def test_login_incorrect_username_correct_password(driver):
    """Test login with incorrect username and correct password and check error message."""
    driver.get(config["base_url"])
    time.sleep(1)
    username = "invalid_user"
    password = config["password"]
    
    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(1)

    assert not login_page.is_logged_in(), "Login succeeded with incorrect username and correct password"
    # Capture the error message displayed on the page
    error_element = driver.find_element("css selector", 'p[data-slot="form-message"]')
    actual_error_message = error_element.text
    expected_invalid_mail_error_message = config["expected_invalid_mail_error_message"]
    print(f"Actual error message: '{actual_error_message}'")
    assert actual_error_message == expected_invalid_mail_error_message, f"Expected error message '{expected_invalid_mail_error_message}', got '{actual_error_message}'"
    print("Login test with incorrect username and correct password executed successfully!")

@pytest.mark.usefixtures("driver")
def test_login_empty_username_empty_password(driver):
    """Test login with empty username and empty password and check error messages."""
    driver.get(config["base_url"])

    username = ""
    password = ""

    login_page = LoginPage(driver)
    login_page.login(username, password)

    time.sleep(1)

    assert not login_page.is_logged_in(), "Login succeeded with empty username and empty password"

    # Capture error messages for both username and password fields
    error_elements = driver.find_elements(
        By.CSS_SELECTOR, 'p[data-slot="form-message"][id$="-form-item-message"]'
    )
    email_error = error_elements[0].text.strip() if len(error_elements) > 0 else ""
    password_error = error_elements[1].text.strip() if len(error_elements) > 1 else ""

    expected_empty_email_error = config["expected_empty_email_error_messge"]
    expected_empty_password_error = config["expected_empty_password_error_message"]

    print(f"Actual email error: '{email_error}'")
    print(f"Actual password error: '{password_error}'")

    assert email_error == expected_empty_email_error, f"Expected email error '{expected_empty_email_error}', got '{email_error}'"
    assert password_error == expected_empty_password_error, f"Expected password error '{expected_empty_password_error}', got '{password_error}'"

    print("Login test with empty username and empty password executed successfully!")
