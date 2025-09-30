from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

class CoachPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    coach_tab = (By.XPATH, "//button[.//span[normalize-space(text())='Coaches']]")
    on_board_coache_button = (By.XPATH, "//button[normalize-space(text())='+ Onboard Coach']")
    coach_first_name_input = (By.XPATH, "//input[@name='coach_firstname' and @placeholder=\"Enter coach's first name\"]")
    coach_last_name_input = (By.XPATH, "//input[@name='coach_lastname' and @placeholder=\"Enter coach's last name\"]")
    date_button = (By.XPATH, "//button[.//span[text()=\"Enter coach's date of birth\"]]")
    year_dropdown = (By.XPATH, "//select[contains(@class, 'rdp-years_dropdown')]")
    date_value_button = (By.XPATH, "//button[normalize-space(text())='5']")
    gender_dropdown = (By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'Select gender')]]")
    email_input = (By.XPATH, "//input[@placeholder=\"Enter coach's email\"]")
    mobile_input = (By.XPATH, "//input[@placeholder=\"Enter coach's mobile number\"]")
    create_button = (By.XPATH, "//button[normalize-space()='Create Coach']")
    cancel_button=(By.XPATH, "//button[text()='Cancel']")

    # def onboard_coach(self, first_name, last_name, year, email, mobile):
    def click_coach_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.coach_tab)).click()
        time.sleep(2)
    def click_on_board_coach_button(self):
        self.wait.until(EC.element_to_be_clickable(self.on_board_coache_button)).click()
    def create_first_name_input(self, first_name):
        self.wait.until(EC.visibility_of_element_located(self.coach_first_name_input)).send_keys(first_name)
        print(f"✅Enter first name{first_name}")
    
    def create_last_name_input(self,last_name):
        self.wait.until(EC.visibility_of_element_located(self.coach_last_name_input)).send_keys(last_name)
        print(f"✅Enter last name{last_name}")

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
        print(f"✅ Select year of birth {year}")

    def click_select_gender_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.gender_dropdown)).click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(2)
        print("✅ Gender selected")
    def create_email_input(self,email):
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        print(f"✅Enter email {email}")

    def create_mobile_input(self,mobile):
        self.wait.until(EC.visibility_of_element_located(self.mobile_input)).send_keys(mobile)
        print(f"✅Enter mobile number {mobile}")

    def click_create_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()
        print("✅ Clicked Create Coach button")

    def clear_field(self, locator):
        # try:
            field = self.wait.until(EC.presence_of_element_located(locator))
            field.clear()
    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()
        print("✅ Clicked Cancel button")

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
       
    def remove_coach_and_capture_error(self):
        js = """
        [...document.querySelectorAll('h3')].forEach(h3 => {
        if (h3.textContent.trim() === 'Jane Smith') {
          const cardHeader = h3.closest('div[data-slot="card-header"]');
          if (cardHeader) {
            const menuBtn = cardHeader.querySelector('svg.lucide-ellipsis-vertical');
             if (menuBtn) {
               const pointerDown = new PointerEvent('pointerdown', { bubbles: true });
               const mouseClick = new MouseEvent('click', { bubbles: true, cancelable: true });
               menuBtn.dispatchEvent(pointerDown);
               menuBtn.dispatchEvent(mouseClick);
               }
             }
         }
        });
          """
        self.driver.execute_script(js)
        time.sleep(2)
        # Step 2: Click on "Remove Athlete"  
        remove_xpath = "//div[@role='menuitem' and normalize-space(text())='Remove Coach']"  
        remove_button = self.wait.until(  
            EC.element_to_be_clickable((By.XPATH, remove_xpath))  
        )  
        remove_button.click()  

        # Step 3: Confirm deletion  
        delete_button_xpath = "//button[normalize-space()='Delete' and contains(@class,'bg-destructive')]"  
        self.wait.until(  
        EC.element_to_be_clickable((By.XPATH, delete_button_xpath))  
           ).click()  
        # Step 4: Capture success message or error toast
        toast_xpath = "//ol[contains(@class, 'toaster')]/li//div[@data-content]"
        toast_text = self.driver.find_element(By.XPATH, toast_xpath).text
        print("Toast message:", toast_text)

   