from asyncio import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SignupPage:
    def __init__(self, driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    #locators   
    signup_link=(By.XPATH,"//button[contains(text(), 'Sign Up')]")
    username_input = (By.XPATH, "//input[@name='email']") 
    password_input = (By.XPATH, "//input[@name='password']")
    confirmpassword_input = (By.XPATH, "//input[@name='confirmPassword']")
    continue_button= (By.XPATH, "//button[contains(text(), 'Continue')]")

    #methods
    def signup(self,email, newpassword, confirm_password):
        self.wait.until(EC.visibility_of_element_located(self.signup_link)).click()
        time.sleep(5)

        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(email)
        time.sleep(5)
        self.wait.until(EC.visibility_of_element_located(self.continue_button)).click()
        time.sleep(5)
        #otp validation manually
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
                if email_cell == email:
                    otp = cells[3].text.strip()
                    print(f"Extracted OTP for {email}: {otp}")
                    break
        if not otp:
            raise Exception(f"OTP not found for email: {email}")
        # Switch back to the main signup tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
       
        # Enter the OTP in the OTP input field
        otp_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='otp' and @inputmode='numeric']"))
        )
        otp_input.send_keys(otp)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
       
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(newpassword)
        self.wait.until(EC.visibility_of_element_located(self.confirmpassword_input)).send_keys(confirm_password)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    