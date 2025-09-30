from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pytest
import re
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)  # Waits up to 10 seconds
  
    # Locators     
    username_input = (By.XPATH, "//input[@name='email']") 
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[contains(text(), 'Continue')]")
    sidebar_span = (By.XPATH, "//button[@data-slot='sidebar-trigger']//span")
    forgot_password_locator = (By.XPATH,"//button[normalize-space(text())='Forgot Password?']")
    signup_link_locator = (By.XPATH, "//button[contains(normalize-space(.), 'Sign Up')]")

 

    def create_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        print(f"Entered username:{username}")
    def create_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password) 
        print(f"Entered password:{password}")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        print("Clicked On Login button")
    

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
                By.XPATH, "/html/body/div[2]/div/div[2]/div/span"
            )))
            toggle_button.click()
            time.sleep(2)

            signout_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[contains(text(), 'Sign Out')]"
            )))
            signout_button.click()
          
        except Exception as e:
            print(f"Error during sign out: {e}")
    def is_forgot_password_displayed(self, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.forgot_password_locator)
            )
            if elem.is_displayed():
                print("✅ 'Forgot Password?' link is displayed")
                return True
            else:
                print("⚠️ 'Forgot Password?' link is present but not visible")
                return False
        except:
            print("❌ 'Forgot Password?' link is NOT present on the page")
            return False
    def is_signup_link_displayed(self, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.signup_link_locator)
            )
            if elem.is_displayed():
                print("✅ 'Sign Up' link is displayed")
                return True
            else:
                print("⚠️ 'Sign Up' link is present but not visible")
                return False
        except:
            print("❌ 'Sign Up' link is NOT present on the page")
            return False