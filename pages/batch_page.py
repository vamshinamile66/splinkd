from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class BatchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


        # Locators
        self.programs_tab = (By.XPATH, "//button[.//span[text()='Programs']]")
        self.add_batch_button=(By.XPATH, "//button[contains(text(), 'Add Batch')]")
        self.batch_name_input=(By.XPATH, "//input[@placeholder='Enter Batch name']")
        self.start_time_input=(By.XPATH,"//input[@name='batch_timings.0.starttime' and @type='time']")
        self.end_time_input=(By.XPATH,"//input[@name='batch_timings.0.endtime' and @type='time']")
        self.save_button=(By.XPATH,"//button[normalize-space()='Save']")
        self.cancel_button=(By.XPATH,"//button[normalize-space()='Cancel']")




    # def add_batch(self, program_name, batch_name, start_time, end_time):
    def click_program_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.programs_tab)).click()
        print("✅Click on program tab")
        time.sleep(4)
    def select_and_click_program_name(self,program_name):
    # Build case-insensitive XPath
        normalized_name = program_name.lower().strip()
        xpath = (
        f"//h6[contains(translate(normalize-space(), "
        f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
        f"'{normalized_name}')]"
    )
        print(f"[INFO] Looking for program: {program_name}")

        try:
            program_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", program_element)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].click();", program_element)
        except Exception as e:
            print(f"[ERROR] Could not find or click program '{program_name}': {e}")
            raise

    def click_add_batch_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_batch_button)).click()
        print("✅clicked on add batch button")
    def create_batch_name(self,batch_name):
        self.wait.until(EC.visibility_of_element_located(self.batch_name_input)).send_keys(batch_name)
        print(f"✅Entered batch name: {batch_name}")
    def select_start_time(self,start_time):
        self.wait.until(EC.visibility_of_element_located(self.start_time_input)).send_keys(start_time)
        print(f"✅Entered start time: {start_time}")
    def select_end_time(self,end_time):  
        self.wait.until(EC.visibility_of_element_located(self.end_time_input)).send_keys(end_time)
        print(f"✅Entered end time: {end_time}")
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()
        print("✅clicked on save button")
    def check_toast_message(self):
        try:
        # Wait for success toast to appear
            success_msg_elem = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-description and contains(text(), 'Batch Creation Successful')]"))
        )
            print("Success message displayed:", success_msg_elem.text.strip())
        except:
            print("Success message not displayed")
            pass

    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()
        print("✅clicked on cancel button")

    def clear_field(self, locator):
        try:
            field = self.wait.until(EC.presence_of_element_located(locator))
            field.clear()
            print(f"✅Cleared field: {locator}")
        except Exception as e:
            print(f"❌ Failed to clear field {locator}: {e}")

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