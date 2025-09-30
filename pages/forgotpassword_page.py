from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Forgotpassword(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)  # Waits up to 10 seconds
    
    #locators
    forgotpassword_link = (By.XPATH, "//button[normalize-space(text())='Forgot Password?']")
    username_input = (By.XPATH, "//input[@placeholder='Enter your email']")
    continue_button = (By.XPATH, "//button[contains(text(), 'Continue')]")
    newpassword_input = (By.XPATH, "//input[@name='password']")
    confirmpassword_input = (By.XPATH, "//input[@name='confirmPassword']")
    submit_button = (By.XPATH, "//button[contains(text(), 'Submit')]")
    resend_button = (By.XPATH, "//button[normalize-space()='Resend']")
    username_input = (By.XPATH, "//input[@name='email']") 
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[contains(text(), 'Continue')]")
    sidebar_span = (By.XPATH, "//button[@data-slot='sidebar-trigger']//span")
    OTP_input=(By.XPATH, "//input[@name='otp' and @inputmode='numeric']")
    verify_otp_header = (By.XPATH, "//h4[normalize-space()='Verify OTP']")
    label_locator = (By.XPATH, "//label[contains(@class,'form-label')]")
    description_locator = (By.XPATH, "//p[contains(@class,'text-sp-subheader')]")
    #methods
    # def forgotpassword(self,username, newpassword, confirmpassword,captch_url):
    def click_forgot_password_link(self):
        self.wait.until(EC.element_to_be_clickable(self.forgotpassword_link)).click()
        print("clicked on forgotpassword link")
        time.sleep(5)
    def create_username(self,username):
        # Re-locate the username input after clicking the forgot password link
        username_input_elem = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_input_elem.send_keys(username)
        print(f"Entered username/email: {username}")
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        print("clicked on continue button")
    def capture_otp(self,username,captch_url):
        time.sleep(2)
        # Switch to new tab and open the OTP admin URL
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(captch_url)
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
    
    def create_new_password(self,newpassword):
        self.wait.until(EC.visibility_of_element_located(self.newpassword_input)).send_keys(newpassword)
        print(f"Entered new password: {newpassword}")
    def create_confirm_password(self,confirmpassword):
        self.wait.until(EC.visibility_of_element_located(self.confirmpassword_input)).send_keys(confirmpassword)
        print(f"Entered confirm password: {confirmpassword}")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        print("clicked on submit button")
    def submit_invalid_otp(self, username, invalid_otp):
        username_input_elem = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_input_elem.clear()
        username_input_elem.send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        otp_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='otp' and @inputmode='numeric']"))
        )
        otp_input.send_keys(invalid_otp)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def enter_otp(self,invalid_otp):
        otp_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='otp' and @inputmode='numeric']"))
        )
        print(f"Entered OTP: {invalid_otp}")
        otp_input.send_keys(invalid_otp)

    def click_continue_button(self, times=1):
        """Click the continue button multiple times."""
        for _ in range(times):
            self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
    def click_continu_button(self):
            self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
            print("clicked on continue button")
    def click_resend_otp_link(self):
        self.wait.until(EC.element_to_be_clickable(self.resend_button)).click()
        print("clicked on resend link")

    def capture_otp_and_return_methode(self,username,captch_url):
        time.sleep(5)
        # Switch to new tab and open the OTP admin URL
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(captch_url)
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
        return {otp}
       

 

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
    def verify_otp_text_and_click_continue(self):
        """If Verify OTP is present, click Continue button."""
        try:
            # Check if Verify OTP is visible
            otp_header = self.wait.until(
                EC.presence_of_element_located(self.verify_otp_header)
            )
            if otp_header.is_displayed():
                print("Verify OTP is present")
                # Click Continue
                self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
                print("Clicked Continue button on Verify OTP screen")
                return True
        except Exception:
            print("Verify OTP not present, skipping")
            return False



    label_locator = (By.XPATH, "//label[@data-slot='form-label']")
    description_locator = (By.XPATH, "//p[contains(@class,'text-sp-subheader')]")

    def compare_label_with_description(self):
        """Check if label name (without *) is present in description text"""

        # Wait for label to be visible
        label_elem = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.label_locator)
        )
        label_text = label_elem.text.replace("*", "").strip()

        # Wait for description text
        desc_elem = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.description_locator)
        )
        desc_text = desc_elem.text.strip()

        print(f"🔹 Label text: {label_text}")
        print(f"🔹 Description text: {desc_text}")

        assert label_text.lower() in desc_text.lower(), \
            f"Label '{label_text}' not found in description: {desc_text}"
        return True
