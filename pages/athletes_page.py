from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
class AthletesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #locators
    athletes_tab = (By.XPATH, "//button[normalize-space(.//span)='Athletes']")
    Actions_dropdown = (By.XPATH, "//button[normalize-space(text())='Actions']")
    onboard_athletes_button =(By.XPATH, "//button[normalize-space()='+ Onboard Athlete']")
    add_Athlete= (By.XPATH, "//div[@role='menuitem' and text()='Add Athlete']")
    first_name_input = ((By.XPATH, "//input[@name='athlete_firstname' and @placeholder=\"Enter athlete's first name\"]"))
    last_name_input = (By.XPATH,"//input[@name='athlete_lastname' and @placeholder=\"Enter athlete's last name\"]")
    date_button = (By.XPATH, "//button[@aria-haspopup='dialog' and .//span[text()=\"Enter athlete's date of birth\"]]")
    year_dropdown=(By.XPATH, "//select[contains(@class, 'rdp-years_dropdown')]")
    date_value_button= (By.XPATH, "//button[normalize-space(text())='5']")
    gender_dropdown=(By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'Select gender')]]")
    email_input = (By.XPATH, "//input[@name='athlete_email' and @placeholder=\"Enter athlete's email\"]")
    mobile_input = (By.XPATH, "//input[@name='athlete_mobile' and @placeholder=\"Enter athlete's mobile number\"]")
    create_button = (By.XPATH, "//button[@type='submit' and text()='Create Athlete']")
    cancel_button=(By.XPATH, "//button[text()='Cancel']")



    # def onboard_athlete(self, first_name, last_name, year,email, mobile): 
    def click_athlete_tab(self):
        # 1. Click on athletes tab
        self.wait.until(EC.element_to_be_clickable(self.athletes_tab)).click()
        time.sleep(2)  
    def click_actions_dropdown(self):
        # 2. Click on 'on action athletes' button
        self.wait.until(EC.element_to_be_clickable(self.Actions_dropdown)).click()
        #select onboard athlete
    def click_athlete_onboard(self):
        self.wait.until(EC.element_to_be_clickable(self.add_Athlete)).click()
        time.sleep(2)
    def create_first_name(self,first_name):
        # 3. Enter first name
        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        print(f"✅ Entered first name: {first_name}")
    def create_last_name(self,last_name):
        # 4. Enter last name
        self.wait.until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)
        print(f"✅ Entered last name: {last_name}")
    def click_and_select_dob(self,year):
        # 5. click on  date of birth 
        self.wait.until(EC.element_to_be_clickable(self.date_button)).click()
        # Wait for the dropdown to be present
        year_dropdown = Select(self.wait.until(EC.presence_of_element_located(self.year_dropdown)))
        # Select year by visible text
        year_dropdown.select_by_visible_text(year)
        # Wait for the date button and click
        self.wait.until(EC.element_to_be_clickable(self.date_value_button)).click()
        time.sleep(1)
        print(f"✅ Selected DOB year: {year}")
    def click_and_select_gender(self):
        # 6. Select gender dropdown
       # Wait for the "Choose a sport" dropdown button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable(self.gender_dropdown)).click()
        time.sleep(2) 
        # Use keyboard to navigate (DOWN + ENTER)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(2)  
        print("✅ Gender Selected")
    def create_email(self,email):
        # 7. Enter email
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        print(f"✅ Entered email: {email}")
    def create_mobile(self,mobile):
        # 8. Enter mobile number
        self.wait.until(EC.visibility_of_element_located(self.mobile_input)).send_keys(mobile)
        print(f"✅ Entered mobile number: {mobile}")
    def click_create_button(self):
        # 9. Click on create button
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()
        print("✅ Clicked Create button")
    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()
        print("✅ Clicked Cancel button")

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


    def remove_athlete_and_capture_error(self):  
       athlete_name = "John Doe"  

    # XPath to locate the ellipsis icon associated with the athlete  
       ellipsis_xpath = f"//div[@data-slot='card'][.//h3[contains(text(), '{athlete_name}')]]//*[name()='svg'][contains(@class, 'lucide-ellipsis-vertical')]"  

    #   try:  
        # Wait for the SVG element to be clickable  
       ellipsis_icon = self.wait.until(  
            EC.element_to_be_clickable((By.XPATH, ellipsis_xpath))  
        )  

        #   try:  
            # Try native Selenium click  
       ellipsis_icon.click()  
        #   except Exception as e:  
        #     print("Native click failed. Trying JavaScript click.")  
       self.driver.execute_script(  
                "arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true }));", ellipsis_icon  
            )  

        # Step 2: Click on "Remove Athlete"  
       remove_xpath = "//div[@role='menuitem' and normalize-space(text())='Remove Athlete']"  
       remove_button = self.wait.until(  
            EC.element_to_be_clickable((By.XPATH, remove_xpath))  
        )  
       remove_button.click()  

        # Step 3: Confirm deletion  
       delete_button_xpath = "//button[normalize-space()='Delete' and contains(@class,'bg-destructive')]"  
       self.wait.until(  
       EC.element_to_be_clickable((By.XPATH, delete_button_xpath))  
           ).click()  

    def check_parent_guardian_heading_displayed(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[contains(text(), 'Parent/Guardian Information')]")
            )
        )
        print("✅ Athlete Age below 18 yrs then Heading appeared:", heading.text)
        return heading.text


