from asyncio import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from pages.base_page import BasePage

class SignupPage(BasePage):
    def __init__(self, driver):
        self.driver=driver
        super().__init__(driver)
        self.wait=WebDriverWait(driver,10)

    #locators   
    signup_link=(By.XPATH,"//button[contains(text(), 'Sign Up')]")
    username_input = (By.XPATH, "//input[@name='email']") 
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[contains(text(), 'Continue')]")
    confirmpassword_input = (By.XPATH, "//input[@name='confirmPassword']")
    continue_button= (By.XPATH, "//button[contains(text(), 'Continue')]")
    otp_input_field=(By.XPATH, "//input[@name='otp' and @inputmode='numeric']")
    resend_button = (By.XPATH, "//button[normalize-space()='Resend']")

    #methods
    def click_signup_link(self):
        self.wait.until(EC.visibility_of_element_located(self.signup_link)).click()
        print("clicked on signup link")
        time.sleep(5)
    def create_username(self,email):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(email)
        print(f"Entered username:{email}")
        time.sleep(5)
    def click_continue_button(self):
        self.wait.until(EC.visibility_of_element_located(self.continue_button)).click()
        print("clicked on continue button")
        time.sleep(2)
    def click_continue_button_for_signup(self):
        self.wait.until(EC.visibility_of_element_located(self.continue_button)).click()
        print("clicked on continue button")
    def capture_otp_and_send_otp(self,captch_url,email):
        #otp validation manually
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
    def create_otp_field(self,otp):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='otp' and @inputmode='numeric']"))).send_keys(otp)
        print(f"Entered otp:{otp}")
    def create_password(self,newpassword):
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(newpassword)
        print(f"Entered password:{newpassword}")  
    def create_confirm_password(self,confirm_password):    
        self.wait.until(EC.visibility_of_element_located(self.confirmpassword_input)).send_keys(confirm_password)
        print(f"Entered confirm password:{confirm_password}")  
    def click_profile_toggle_button(self):
        toggle_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "/html/body/main/div[1]/div/div[2]/div")))
        toggle_button.click()
        time.sleep(2)
    def clear_field_signup(self, locator):
        field = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].value = '';", field)
    def logout(self):
        try:
            signout_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[contains(text(), 'Sign Out')]" )))
            signout_button.click()
            print("Clicked on Sign Out button")
        except Exception as e:
            print(f"Error during sign out: {e}")
        
    def is_logged_in(self):
        try:
            # Wait until URL changes to a known logged-in state
            self.wait.until(lambda driver: "organisation" in driver.current_url)
            return "organisation" in self.driver.current_url
        
        except Exception:
            return False
    def capture_and_compare_profile_email(self, expected_email):
        try:
            profile_email_elem = self.wait.until(
                EC.visibility_of_element_located(((By.XPATH, "//p[contains(@class,'break-words')]"))
            ))
            email = profile_email_elem.text.strip()
            actual_email = email.replace("!", "").strip()
            print(f"Expected Email: {expected_email}, Actual Email: {actual_email}")
            return expected_email == actual_email
        except Exception as e:
            print(f"Error verifying email: {e}")
            return False
    def click_resend_otp_link(self):
        self.wait.until(EC.element_to_be_clickable(self.resend_button)).click()
        print("clicked on resend link")


    def check_resend_otp_timer(self):
         # Step 1: Verify "Resend in" text is displayed (not clickable)
            resend_in_locator = (By.XPATH, "//span[contains(text(),'Resend in')]")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(resend_in_locator)
            )
            print("✅ Resend timer is displayed initially.")

    def check_resend_otp_clickable(self):
            # Step 2: Wait until "Resend OTP" link becomes clickable
            resend_otp_link = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.resend_button)
            )
            assert resend_otp_link.is_enabled(), "❌ Resend OTP link is not clickable after countdown!"
            print("✅ Resend OTP link is clickable after timer finished.")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        print("Clicked On Login button")
    
    
    def get_displayed_email(self):
        """Fetch the displayed (disabled) email value dynamically."""
        email_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        return email_elem.get_attribute("value")

            