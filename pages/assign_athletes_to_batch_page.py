import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
class AssignAthletesToBatchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    programs_tab = (By.XPATH, "//button[.//span[text()='Programs']]")
    ADD_ATHLETE_BTN = (By.XPATH, "//button[contains(.,'+ Add Athlete')]")
    SEARCH_BTN = (By.XPATH, "//button[contains(.,'Select athlete...')]")
    ATHLETE_SEARCH_INPUT = (By.XPATH, "//input[@type='text' and @placeholder='Search athletes...']")
    ATHLETE_RADIO = (By.XPATH, "//div[@class='mr-2 mt-1 size-4 border rounded-full p-0.5 border-primary']")
    PAYMENT_DROPDOWN = (By.XPATH, "//button[@role='combobox' and .//span[contains(.,'Select payment status')]]")
    FULLY_PAID_OPTION = (By.XPATH, "//div[contains(text(),'Fully Paid')]")
    ADD_ATHLETE_SUBMIT = (By.XPATH, "//button[@type='submit' and text()='Add Athlete']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(),'Athlete added to batch successfully')]") 
    add_Athlete_dropdown= (By.XPATH, "//div[@data-slot='dropdown-menu-item' and text()='Add Athlete']")
    Actions_dropdown = (By.XPATH, "//button[normalize-space(text())='Actions']")
    Internal_ATHLETE_TAB = (By.XPATH, "//div[@role='group' and @aria-roledescription='slide']//button[normalize-space()='Athletes']")
    # Actions

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
    def click_actions_dropdown(self):
        # 2. Click on 'on action athletes' button
        self.wait.until(EC.element_to_be_clickable(self.Actions_dropdown)).click()
        #select onboard athlete
    def click_athlete_onboard(self):
        self.wait.until(EC.element_to_be_clickable(self.add_Athlete_dropdown)).click()
        time.sleep(2)
    def click_program_athlete_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.Internal_ATHLETE_TAB)).click()
        print("[INFO] Clicked program Athlete tab")
    def click_add_athlete(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_ATHLETE_BTN)).click()
        print("[INFO] Clicked Add Athlete button")
    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
        print("[INFO] Clicked Search Athlete button")
    def search_and_select_athlete(self, athlete_name):
        search_input = self.wait.until(EC.presence_of_element_located(self.ATHLETE_SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(athlete_name)
        self.wait.until(EC.element_to_be_clickable(self.ATHLETE_RADIO)).click()
        print(f"[INFO] Searched and selected athlete: {athlete_name}")
        time.sleep(1)

    def select_payment_status_via_keys(self, status_text):
        wait = WebDriverWait(self.driver, 10)
        # Step 1: Click Payment Status dropdown (anchor by label)
        dropdown = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, "//label[contains(text(),'Payment Status')]/following::button[@role='combobox'][1]"
            )))
        dropdown.click()
        # Step 2: Wait for dropdown listbox and click the matching option
        option = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, f"//div[@role='listbox']//div[@role='option' and normalize-space()='{status_text}']"
            )))
        option.click()
    
    def click_add_athlete_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_ATHLETE_SUBMIT)).click()
        print("[INFO] Clicked Add Athlete submit button")
    def get_success_message_text(self):
        """Wait and retry to get success message text"""
        retries = 3
        last_message = ""
        for attempt in range(retries):
            try:
                element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
                last_message = element.text
                if last_message.strip() != "":
                    return last_message
            except:
                pass
            time.sleep(2)  # retry wait
        return last_message
