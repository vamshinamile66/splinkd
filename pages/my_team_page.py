from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

class MyTeamPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    my_team_tab = (By.XPATH, "//button[.//span[normalize-space(text())='My Team']]")
    create_team_button = (By.XPATH, "//button[normalize-space(text())='+ Create Team Member']")
    first_name_input = (By.XPATH, "//input[@name='firstname' and @placeholder=\"Enter first name\"]")
    last_name_input = (By.XPATH, "//input[@name='lastname' and @placeholder=\"Enter last name\"]")
    date_button = (By.XPATH, "//button[.//span[text()='Select date of birth']]")
    y_dropdown = (By.XPATH, "//select[contains(@class, 'rdp-years_dropdown')]")
    m_dropdown=(By.CSS_SELECTOR, "select.rdp-months_dropdown")
    date_value_button = (By.XPATH, "//button[@aria-label='Monday, August 5th, 1985, selected']")
    gender_dropdown = (By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'Select gender')]]")
    email_input = (By.XPATH, "//input[@placeholder=\"Enter email\"]")
    mobile_input = (By.XPATH, "//input[@placeholder=\"Enter mobile number\"]")
    create_button = (By.XPATH, "//button[normalize-space()='Create']")
    #Signup locators   
    signup_link=(By.XPATH,"//button[contains(text(), 'Sign Up')]")
    username_input = (By.XPATH, "//input[@name='email']") 
    password_input = (By.XPATH, "//input[@name='password']")
    confirmpassword_input = (By.XPATH, "//input[@name='confirmPassword']")
    continue_button= (By.XPATH, "//button[contains(text(), 'Continue')]")
    cancel_button=(By.XPATH, "//button[text()='Cancel']")

    # def onboard_team(self, first_name, last_name, month, day , year, email, mobile):
    def click_my_team_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.my_team_tab)).click()
        time.sleep(2)
        print("Clicked My Team tab")
    def click_create_new_team_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_team_button)).click()
        print("Clicked Create Team Member button")
        time.sleep(2)
    def create_first_name(self,first_name):
        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        print("Entered first name:", first_name)
    def create_last_name(self,last_name):
        self.wait.until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)
        print("Entered last name:", last_name)

    def click_and_select_dob(self,month,day,year):
         # 1. Click on calendar button
        calendar_btn = self.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Select date of birth']]"))
    )
        calendar_btn.click()
        print("Clicked Select date of birth button")
      # # 2. Click year dropdown & select year
      # Wait until the <select> exists in DOM
        year_dropdown = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.y_dropdown))
       # Use Select to choose year
        select = Select(year_dropdown)
        select.select_by_visible_text(year)
        print("Selected year:", year)
        # 3. Click month dropdown & select month
        month_dropdown = self.driver.find_element(By.CSS_SELECTOR, "select.rdp-months_dropdown")
        Select(month_dropdown).select_by_value(month) 
        print("Selected month:", month)
        # --- Select Day ---
        day_xpath = f"//button[normalize-space(text())='{day}']"
        day_element = self.wait.until(
        EC.element_to_be_clickable((By.XPATH, day_xpath)))
        day_element.click()
        print("Selected day:", day)

    def click_select_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.gender_dropdown)).click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(2)
        print("Selected gender")
    def create_email(self,email):
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        print("Entered email:", email)
    def create_mobile(self,mobile):
        self.wait.until(EC.visibility_of_element_located(self.mobile_input)).send_keys(mobile)
        print("Entered mobile number:", mobile)
    def Click_overview_toggle(self):
        # Click the input related to "Overview"
        overview_switch = self.driver.find_element(By.XPATH, "//h6[text()='Overview']/following-sibling::div//button[@role='switch']")
        overview_switch.click()
        time.sleep(2)
        print("Clicked Overview input (checkbox)")
    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()
        print("Clicked Create button")
    def clear_field(self, locator):
            field = self.wait.until(EC.presence_of_element_located(locator))
            field.clear()
    def toast_message(self, message, timeout=10):
      try:
          # Use string formatting to insert the message parameter into the XPath
          toast = WebDriverWait(self.driver, timeout).until(
              EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{message}')]"))
          )
          # Print the toast message
          print("Toast appeared:", toast.text)
          return toast.text
      except Exception as e:
          print(f"Error: {str(e)}")
          return None
    def validation_messages(self):
              errors = {}
              error_elements = self.driver.find_elements(By.CSS_SELECTOR, "p.text-destructive")

              for elem in error_elements:
                  error_text = elem.text.strip()
                  if not error_text:
                      continue

                  # Find the nearest input/label above the error message
                  field_name = "Unknown field"
                  try:
                      label_elem = elem.find_element(By.XPATH, "./preceding::label[1]")
                      field_name = label_elem.text.strip()
                  except:
                      try:
                          input_elem = elem.find_element(By.XPATH, "./preceding::input[1]")
                          field_name = input_elem.get_attribute("placeholder") or "Unknown field"
                      except:
                          pass

                  errors[field_name] = error_text
                  print("Mandatory field validations are captured:")
                  print(f"{field_name}: {error_text}")

              return errors


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
        print("Clicked on academy Sign Out button")
    #methods
    def signup_team(self, email, password, confirm_password, captch_url):
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
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(self.confirmpassword_input)).send_keys(confirm_password)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        try:
            success_msg = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'success') or contains(text(), 'successfully')]"))
            )
            print("Success message displayed:", success_msg.text)
            time.sleep(5)
        except Exception:
            print("Success message is not displayed")
            pass
        # Step 1: Click on profile avatar
        profile_avatar = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-slot='avatar']"))
        )
        profile_avatar.click()
        print("Clicked on Profile Avatar")
        #capture the team email
        email_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='mt-1 text-xs text-black break-words leading-none']"))
        )
        displayed_email = email_element.text.strip()
        print(f"displayed email: {displayed_email}")
        print("Onborded team email:", email)

        # compare emails (ignore case + whitespace)
        if displayed_email.lower().strip() == email.lower().strip():
         print("✅ Email matched successfully!")
        else:
         print(f"❌ Email mismatch! Expected: {email}, Got: {displayed_email}")

        # for pytest assertion
        assert displayed_email.lower().strip() == email.lower().strip(), \
        f"Email mismatch! Expected: {email}, Got: {displayed_email}"

        # comapre assigned moudles displayed or not
       # Expected tab names
        expected_tabs = ["OVERVIEW"]

    # Locate only sidebar menu items (left side)
        # Correct way to unpack locator tuple
        buttons = self.driver.find_elements(By.XPATH, "//button[@data-slot='sidebar-menu-button']//span")
        all_tabs = [btn.text.strip() for btn in buttons if btn.text.strip()]
        print("Displayed Modules List", all_tabs)

    # Count check
        assert len(all_tabs) == len(expected_tabs), \
        f"Tab count mismatch! Expected {len(expected_tabs)} but found {len(all_tabs)}"
        print("Assigned and displayed modules count matched")
    # Text check
        assert all_tabs == expected_tabs, \
        f"Tab names mismatch! Expected {expected_tabs} but got {all_tabs}"
        print("Assigned modules and displayed modules are same")