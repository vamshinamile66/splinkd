from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pytest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Waits up to 10 seconds
  
    # Locators     
    username_input = (By.XPATH, "//input[@name='email']") 
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[contains(text(), 'Continue')]")

    # Login method
    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def is_logged_in(self, expected_email=None):
        try:
            # Wait until URL changes to a known logged-in state
            self.wait.until(lambda driver: "manage-organisation" in driver.current_url)
            if expected_email:
                # Wait for profile/email element to be visible
                toggle_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/span"
                     )))
                toggle_button.click()
                time.sleep(2)
                profile_email_elem = self.wait.until(
                    EC.visibility_of_element_located((
                        By.XPATH, "//div[contains(@class, 'text-xs') and contains(text(), '@')]"
                    ))
                )
                actual_email = profile_email_elem.text.strip()
                return expected_email == actual_email
            return "manage-organisation" in self.driver.current_url
        except Exception:
            return False

    def signout(self):
        try:
            toggle_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/span"
            )))
            toggle_button.click()
            time.sleep(2)

            signout_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[contains(text(), 'Sign Out')]"
            )))
            signout_button.click()
          
        except Exception as e:
            print(f"Error during sign out: {e}")
   # ..existing code...

    def forgotpassword_invalid_email(self, username):
        self.wait.until(EC.element_to_be_clickable(self.forgotpassword_link)).click()
        time.sleep(2)
        username_input_elem = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_input_elem.clear()
        username_input_elem.send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        # Wait for the error message to appear (update selector as needed)
        error_elem = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-type="error"]'))
        )
        error_text = error_elem.text
        print(f"Error message for non-existing email: {error_text}")
        return error_text
# ...existing code...