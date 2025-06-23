from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Forgotpassword:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Waits up to 10 seconds
    
    #locators
    forgotpassword_link = (By.XPATH, "//button[normalize-space(text())='Forgot Password?']")
    username_input = (By.XPATH, "//input[@name='email']") 
    continue_button = (By.XPATH, "//button[contains(text(), 'Continue')]")
    newpassword_input = (By.XPATH, "//input[@name='password']")
    confirmpassword_input = (By.XPATH, "//input[@name='confirmPassword']")
    submit_button = (By.XPATH, "//button[contains(text(), 'Submit')]")

    #methods
    def forgotpassword(self,username,newpassword,confirmpassword):
        self.wait.until(EC.element_to_be_clickable(self.forgotpassword_link)).click()
        time.sleep(5)
        # Re-locate the username input after clicking the forgot password link
        username_input_elem = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_input_elem.send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        # Switch to new tab and open the OTP admin URL
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://splink-api.meenestham.in/v1/admin/otp-cache/list")
        time.sleep(2)

        # Wait for the OTP table to load and extract the OTP value for the matching email
        table = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        rows = table.find_elements(By.XPATH, ".//tbody/tr")
        otp = None
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 8:
                email_cell = cells[6].text.strip()
                if email_cell == username:
                    otp = cells[3].text.strip()
                    print(f"Extracted OTP for {username}: {otp}")
                    break
        if not otp:
            raise Exception(f"OTP not found for email: {username}")
        # Switch back to the main signup tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
       
        # Enter the OTP in the OTP input field
        otp_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='otp' and @inputmode='numeric']"))
        )
        otp_input.send_keys(otp)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        # Wait for the popup to appear and capture its text
        popup = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-type="error"]')))
        popup_text = popup.text
        print(f"Popup text: {popup_text}")
        time.sleep(2)

        self.wait.until(EC.visibility_of_element_located(self.newpassword_input)).send_keys(newpassword)
        self.wait.until(EC.visibility_of_element_located(self.confirmpassword_input)).send_keys(confirmpassword)
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()

    def forgotpassword_invalid_email(self, username):
        self.wait.until(EC.element_to_be_clickable(self.forgotpassword_link)).click()
        time.sleep(1)
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



