from asyncio import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time 
import re
import os
from selenium.common.exceptions import TimeoutException

class RegisterAcademyPage:
    def __init__(self, driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

#locators   
    signup_link=(By.XPATH,"//button[contains(text(), 'Sign Up')]")
    username_input = (By.XPATH, "//input[@name='email']") 
    password_input = (By.XPATH, "//input[@name='password']")
    confirmpassword_input = (By.XPATH, "//input[@name='confirmPassword']")
    continue_button= (By.XPATH, "//button[contains(text(), 'Continue')]")
#loactors Academy registration
    academy_name_input = (By.XPATH, "//input[@name='academy_name']")
    mobile_number_input = (By.NAME, "mobile_no")
    location_input = (By.XPATH, "//input[@placeholder='Search branch address...']")
    sports_dropdown = (By.XPATH, "//button[contains(.,'Select sports')]")    
    file_upload_input = (By.XPATH, "//label[contains(., 'Choose File')]//input[@type='file']")
    logo_upload=(By.NAME, "logo")
    #  logo_upload=(By.XPATH, "//label[contains(., 'Upload Logo')]/input[@type='file']")
    next_button = (By.XPATH, "//button[normalize-space()='Next']")
    create_profile_button = (By.XPATH, "//button[normalize-space()='Create Profile']")
    previous_button = (By.XPATH, "//button[normalize-space(text())='Previous']")
  
  
    #methods
    def signup(self,email, newpassword, confirm_password,captch_url):
        self.wait.until(EC.visibility_of_element_located(self.signup_link)).click()
        print("Signup page is displayed")
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.username_input)).send_keys(email)
        print("Email is entered:", email)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        # ✅ Capture toast after clicking continue (if any)
        self.toast_message("Please verify")
        #otp validation manually
        # Switch to new tab and open the OTP admin URL
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(captch_url)
        time.sleep(2)
        print("Switched to OTP admin tab")
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
                    print("OTP is extracted from admin page")
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
        print("OTP is entered in the input field")
          
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
    
        print("Clicked on Continue button after entering OTP")
        # ✅ Capture toast after OTP submit (if any)
        self.toast_message("successfully")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.password_input)).send_keys(newpassword)
        print("New password is entered")
        self.wait.until(EC.element_to_be_clickable(self.confirmpassword_input)).send_keys(confirm_password)
        print("Confirm password is entered")
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
        print("Clicked on Continue button after entering passwords")
        time.sleep(2)
        self.toast_message("successfully")
  
  #--------------------------Academy registration methods--------------------------
    # Step 1: Enter academy name
    def academy_name_field(self, academy_name):
        time.sleep(1)
        academy_input = self.wait.until(
         EC.element_to_be_clickable(self.academy_name_input)
    )
        self.driver.execute_script("arguments[0].value = '';", academy_input)
        academy_input.send_keys(academy_name)
        print("academy regitration started")
        print("Academy name entered:", academy_name)

    # 3. Enter mobile number
    def mobile_number_field(self,mobile_number):
      mobile_input = self.wait.until(
        EC.element_to_be_clickable(self.mobile_number_input)
    )
      self.driver.execute_script("arguments[0].value = '';", mobile_input)
      mobile_input.send_keys(mobile_number)
      print("mobile number entered:", mobile_number)

    # 4. Select sports
    def select_sports(self,sports):
      self.wait.until(EC.element_to_be_clickable(
        self.sports_dropdown)
    ).click()
      time.sleep(2)
      xpath = f"//label[.//span[text()='{sports}']]//button"
      self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
      print("Sport selected:", sports)
      time.sleep(2)
      # click outside to close
      self.driver.find_element(By.TAG_NAME, "body").click()
      time.sleep(2)

    def upload_file(self, file_path: str) -> str:
        """Uploads a file and returns the uploaded file name."""
        try:
            upload_input = self.driver.find_element(*self.file_upload_input)
            upload_input.send_keys(file_path)
            file_name = file_path.split("/")[-1]
            print(f"📂 File uploaded: {file_name}")
            return file_name
        except Exception as e:
                print(f"❌ File upload failed: {e}")
                return None
    #uploading multiple files at once
    def upload_files(self, *file_paths):
        upload_file_input = self.driver.find_element(*self.file_upload_input)
        files_to_upload = "\n".join(file_paths)   # join all with newlines
        upload_file_input.send_keys(files_to_upload)
        print("Files uploaded:", file_paths)
 
        
    # def is_file_uploaded(self, file_name, timeout=10):
    #     """Check if uploaded file name is displayed on UI."""
    #     try:
    #         uploaded_file = WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{file_name}')]"))
    #         )
    #         print(f"✅ Uploaded file is displayed: {uploaded_file.text}")
    #         return True
    #     except Exception:
    #         print(f"❌ Uploaded file '{file_name}' is not displayed")
    #         return False
   

    def delete_file(self, file_name: str) -> bool:
        """Click delete button for given file and confirm deletion."""
        try:
            # Locate the file container by its name
            file_row = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    f"//*[contains(text(), '{file_name}') or @title='{file_name}']/ancestor::div[contains(@class,'group')]"
                ))
            )

            # Find the delete button inside that container and wait until clickable
            delete_btn = WebDriverWait(file_row, 10).until(
                EC.element_to_be_clickable((By.XPATH, ".//button[normalize-space()='Delete']"))
            )

            # Click the delete button
            delete_btn.click()

            # Wait until the file name disappears from the DOM
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((
                    By.XPATH,
                    f"//*[contains(text(), '{file_name}') or @title='{file_name}']"
                ))
            )

            print(f"✅ File '{file_name}' deleted successfully")
            return True

        except Exception as e:
            print(f"❌ Could not delete file '{file_name}' → {e}")
            return False


    def is_choose_file_option_available(self) -> bool:
        """Check if 'Choose File' option is available."""
        try:
            choose_label = self.driver.find_element(By.XPATH, "//label[contains(., 'Choose File')]")
            available = choose_label.is_displayed() and choose_label.is_enabled()
            print(f"ℹ️ 'Choose File' visible: {available}")
            return available
        except:
            print("ℹ️ 'Choose File' option not found")
            return False

    def upload_logo(self,logo_path):
      upload_logo_input = self.driver.find_element(*self.logo_upload)
      upload_logo_input.send_keys(logo_path)
      print("Logo uploaded:", logo_path)

    def next_button_click(self):
      next_btn = self.wait.until(EC.element_to_be_clickable(self.next_button))
      next_btn.click()
      time.sleep(2)
      print("Clicked on next button")
      # self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
    
    def search_and_select_location(self, location):
    # 7. Search for location and select
      search_input = self.wait.until(
        EC.element_to_be_clickable(self.location_input)
    )
      self.driver.execute_script("arguments[0].value = '';", search_input)
      search_input.send_keys(location)
      time.sleep(2)
      print("Location entered in search:", location)
      search_input.send_keys(Keys.ARROW_DOWN)
      search_input.send_keys(Keys.ENTER)
      time.sleep(2)

    # 9. Click Create Profile
    def click_create_profile(self):
     # Click Create Profile
      create_btn = WebDriverWait(self.driver, 15).until(
        EC.element_to_be_clickable(self.create_profile_button))
      create_btn.click()   
    def normalize_error(self, text: str) -> str:
        """Normalize validation message text (lowercase, strip punctuation/spaces)."""
        return re.sub(r'[^a-z]', '', text.lower())
    def validation_academy_registration(self):
        """
        Collects validation errors from Academy Registration form.
        Returns dictionary: {field_label: normalized_error_message}
        """
        errors = {}
        error_elements = self.driver.find_elements(By.CSS_SELECTOR, "p.text-destructive")

        if error_elements:
            print("Mandatory field validations are captured:")

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
            # ✅ Clean field name (remove newline + * + extra spaces)
            field_name = field_name.replace("\n", " ").replace("*", "").strip()
            # Normalize error before storing
            normalized = self.normalize_error(error_text)
            errors[field_name] = normalized

            # ✅ Print neatly (only once)
            print(f"{field_name}: {error_text}")

        return errors
    def clear_field(self, locator):
            field = self.wait.until(EC.presence_of_element_located(locator))
            field.clear()

    def is_branch_error_displayed(self):
        self.branch_error_message = (By.XPATH, "//p[contains(text(),'At least one branch location is required')]")
        try:
            return self.driver.find_element(*self.branch_error_message).is_displayed()
        except:
            return False
        
    def click_previous(self):
        prev_btn = self.wait.until(EC.element_to_be_clickable(self.previous_button))
        prev_btn.click()
        time.sleep(2)
        print("Clicked Previous to go back to academy details")

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

    def logout(self):
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