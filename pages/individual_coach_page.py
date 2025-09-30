 
from asyncio import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
    programs_tab = (By.XPATH, "//button[.//span[text()='Programs']]")  
    login_button = (By.XPATH, "//button[contains(text(), 'Continue')]")
    #methods
    def signup(self,email, newpassword, confirm_password,captch_url):
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
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
       
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(newpassword)
        self.wait.until(EC.visibility_of_element_located(self.confirmpassword_input)).send_keys(confirm_password)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        try:
            success_msg = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'success') or contains(text(), 'successfully')]"))
            )
            print("Success message displayed:", success_msg.text)
        except Exception:
            print("Success message is not displayed")
            pass
        time.sleep(5)
   #login shoulde be removed after 
   # Login method
    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        time.sleep(5)  


    def click_programs_tab(self):  
        self.wait.until(EC.element_to_be_clickable(self.programs_tab)).click() 
        print("Clicked on Programs tab")
    
    # Mark attendence and verify success message
    def test_mark_attendance(self, program_name, athlete_name):
      wait = WebDriverWait(self.driver, 20)
      time.sleep(5)
      # Fetch all program names before locating the specific one
      program = self.wait.until(
      EC.element_to_be_clickable((
        By.XPATH,
        f"//*[contains(translate(normalize-space(text()), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{program_name.lower()}')]"
    ))
)
      program.click()
      print(f"Clicked program: {program_name}")
      time.sleep(5)
    #  Locate athlete row and click 'P' button
      athlete_row = self.wait.until(
      EC.element_to_be_clickable((
            By.XPATH,
            f"//div[contains(@class,'flex') and .//div[normalize-space(text())='{athlete_name}']]//button[normalize-space(text())='P']"
        ))
    )
      athlete_row.click()
      print(f"Marked attendance (P) for: {athlete_name}")

    # 4. Click on Save button
      save_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and normalize-space()='Save']"))
    )
      save_button.click()
      print("✅ Clicked Save")

    # 5. Verify success message
      success_msg = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Attendance marked successfully')]"))
    )
      assert "Attendance marked successfully" in success_msg.text
      print("🎉 Attendance marked successfully!")
      time.sleep(5)
    def logout(self):
        # Step 1: Click on profile avatar
        profile_avatar = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-slot='avatar']"))
        )
        profile_avatar.click()
        print("Clicked on Profile Avatar")
        # Step 2: Click on Sign Out button
        signout_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Sign Out']"))
        )
        signout_btn.click()
        time.sleep(4)
        print("Clicked on Sign Out button")