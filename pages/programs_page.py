from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class ProgramsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


# Locators  
    programs_tab = (By.XPATH, "//button[.//span[text()='Programs']]")  
    create_program_button =(By.XPATH,"//button[.//span[contains(normalize-space(), 'Create Program')]]")
    program_title_input = (By.XPATH, "//input[@name='programname']")  
    program_desc_input = (By.XPATH, "//textarea[@name='description']")  
    program_price_input = (By.XPATH, "//input[@name='fee']")  
    sport_dropdown = (By.XPATH, "//button[.//span[text()='Choose a sport']]")  
    best_fit_button = (By.XPATH, "//button[normalize-space(text())='Beginner']")  
    next_button = (By.XPATH, "//button[normalize-space(text())='Next']")  
    program_cover_image_upload_input = (By.XPATH, "//input[@type='file' and @name='program_poster']")  
    create_button = (By.XPATH, "//button[normalize-space(text())='Create']")  
    success_msg = (By.XPATH, "//h5[normalize-space()='Program Created Successfully']")  
    no_button = (By.XPATH, "//button[@data-slot='button' and normalize-space()='No']")  
    cancel_button=(By.XPATH, "//button[normalize-space()='Cancel']")

    search_input = (By.XPATH, "//input[contains(@placeholder, 'Search programs')]")  

    menu_button_xpath = ".//button[contains(@aria-haspopup,'menu')]"  
    edit_option_xpath = "//*[contains(@id, 'radix-_r_')]/div[1]"  
    update_button = (By.XPATH, "//button[normalize-space()='Update']") 
    #program details page
    program_title = (By.XPATH, "//h2[contains(@class,'font-semibold')]")
    program_description_toggle= (By.XPATH, "//span[normalize-space(text())='Program Description']")
    program_description_text= (By.XPATH,"//div[@data-slot='scroll-area-viewport']//div[last()]")
    
    def click_programs_tab(self):  
        self.wait.until(EC.element_to_be_clickable(self.programs_tab)).click()  
        print("✅ Clicked Programs tab")
        time.sleep(2)
    def click_create_new_program_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_program_button)).click() 
        print("✅ Clicked Create New Program button")   
        time.sleep(2)
    def create_program_title(self,title):
        self.wait.until(EC.visibility_of_element_located(self.program_title_input)).send_keys(title) 
        print("✅Entered program title:{title}")
    def create_program_desc(self,description): 
        self.wait.until(EC.visibility_of_element_located(self.program_desc_input)).send_keys(description)  
        print("✅Entered program description:{description}")
    def create_program_price(self,price):
        self.wait.until(EC.visibility_of_element_located(self.program_price_input)).send_keys(price)  
        print("✅Entered program price:{price}")
    def select_sports_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.sport_dropdown)).click()  
        time.sleep(1)  
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform() 
        print("✅ Selected sport from dropdown")
    def select_bestfit_level(self):
        self.wait.until(EC.element_to_be_clickable(self.best_fit_button)).click() 
        print("✅ Selected best fit level")
    def click_next_button(self): 
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click() 
        print("✅ Clicked Next button")
    def upload_cover_image_and_create(self,cover_image_path): 
        self.wait.until(EC.presence_of_element_located(self.program_cover_image_upload_input)).send_keys(cover_image_path)  
        print(f"✅ Uploaded cover image: {cover_image_path}")
    def click_program_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()  
        print("✅ Clicked Create button")
    def is_success_message_displayed(self):
        try:  
            msg = self.wait.until(EC.visibility_of_element_located(self.success_msg))  
            print("✅ Program created:", msg.text)  
            self.wait.until(EC.element_to_be_clickable(self.no_button)).click()  
        except:  
            print("⚠️ Program success message not found.")  

    def click_cancel_button(self):
         self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click() 
         print("✅ Clicked Cancel button") 

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
    
    def clear_field(self, locator):
        try:
            field = self.wait.until(EC.presence_of_element_located(locator))
            field.clear()
            print(f"✅ Cleared field: {locator}")
        except Exception as e:
            print(f"❌ Failed to clear field {locator}: {e}")

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


    def search_program(self, program_name):  
        search = self.wait.until(EC.visibility_of_element_located(self.search_input))  
        search.clear()  
        search.send_keys(program_name + Keys.RETURN)  
        print(f"✅ Searched for program: {program_name}")
        time.sleep(3)  

    def click_program_by_name(self, program_name):
            # Debug all available program names
        headings = self.driver.find_elements(By.TAG_NAME, "h6")
        print("[DEBUG] Available <h6> texts:")
        for h in headings:
          print("-", h.text.strip())

    # Build case-insensitive XPath
        normalized_name = program_name.lower().strip()
        xpath = (
        f"//h6[contains(translate(normalize-space(), "
        f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
        f"'{normalized_name}')]"
    )
        print(f"[INFO] Looking for program using XPath: {xpath}")

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
        print(f"✅ Clicked on program: {program_name}")
       
    # Methods
    def get_program_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.program_title)).text.strip()

    def click_medal_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.program_description_toggle)).click()
        time.sleep(2)

    # def get_program_description(self):
        
        # # Wait for description to appear
        # desc_element = self.wait.until(
        #     EC.visibility_of_element_located(self.program_description_text)
        # )
        # return desc_element.text.strip()

    # def click_3_dot_menu(self, program_name):
    #     print(f"Looking for program card with title: {program_name}")
    #     # program_card_xpath = f"//h6[contains(normalize-space(), '{program_name}')]/ancestor::div[contains(@class,'rounded-xl')]"
    #     menu_icon_xpath = "//*[contains(@id, 'radix')]"



    #     try:
            
    #         menu_icon = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, menu_icon_xpath))
    #         )
    #         self.driver.execute_script("arguments[0].scrollIntoView(true);", menu_icon)      
    #         menu_icon.click()
    #         print("✅ Clicked 3-dot menu")
    #     except Exception as e:
    #         print(f"❌ Could not find card or menu for program: '{program_name}'")
    #         raise e


    # def click_edit_option(self):  
    #     try:  
    #         edit_option = self.wait.until(  
    #             EC.visibility_of_element_located((By.XPATH, self.edit_option_xpath))  
    #         )  
    #         edit_option.click()  
    #         print("✅ Edit clicked.")  
    #     except Exception as e:  
    #         self.driver.save_screenshot("edit_option_error.png")  
    #         print("❌ Edit option failed.")  
    #         raise e  

    # def update_description_and_save(self, new_text="edited description"):  
    #     desc_box = self.wait.until(EC.presence_of_element_located(self.program_desc_input))  
    #     desc_box.clear()  
    #     desc_box.send_keys(new_text)  
    #     self.wait.until(EC.element_to_be_clickable(self.update_button)).click()  
    #     print("✅ Program updated.")
