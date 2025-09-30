import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class AssignCoachToBatchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    Internal_COACHES_TAB = (By.XPATH, "//div[@role='group' and @aria-roledescription='slide']//button[normalize-space()='Coaches']")
    programs_tab = (By.XPATH, "//button[.//span[text()='Programs']]")
    ADD_COACH_BUTTON = (By.XPATH, "//button[contains(.,'+ Add Coach')]")
    EXISTING_COACH_CHECKBOX = (By.XPATH, "//*[@id='radix-_r_1g_']/fieldset/form/div[2]/div/div/div/div[1]/label/input")
    CONFIRM_ADD_COACH_BUTTON = (By.XPATH, "//button[normalize-space()='Add Coach']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(),'Coach added to batch successfully')]")


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
    # Actions
    def click_coaches_tab(self):
        logger.info("[STEP] Clicking Coaches tab")
        print("[INFO] Clicking Coaches tab")
        self.wait.until(EC.element_to_be_clickable(self.Internal_COACHES_TAB)).click()

    def click_add_coach_button(self):
        logger.info("[STEP] Clicking '+ Add Coach' button")
        print("[INFO] Clicking '+ Add Coach' button")
        self.wait.until(EC.element_to_be_clickable(self.ADD_COACH_BUTTON)).click()

  
    def click_coach_by_name(self, name="Jane Smith"):
        coach_locator = (By.XPATH, f"//div[@class='text-sm' and normalize-space(text())='{name}']")
        element = self.wait.until(EC.element_to_be_clickable(coach_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        print(f"[INFO] Selected coach: {name}")


    def click_confirm_add_coach(self):
        logger.info("[STEP] Clicking final 'Add Coach' button")
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_ADD_COACH_BUTTON)).click()
        print("[INFO] Clicked final 'Add Coach/submit' button")
    def get_success_message_text(self):
        logger.info("[STEP] Waiting for success message")
        msg = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
        logger.info(f"[SUCCESS] Success message found: {msg}")
        print("[INFO] Success message found:", msg)
        return msg
        
 
