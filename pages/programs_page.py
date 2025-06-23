from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class ProgramsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    programs_tab = (By.XPATH, "//a[contains(text(), 'Programs')]")
    program_title_input = (By.XPATH, "//input[@name='programTitle']")
    program_desc_input = (By.XPATH, "//textarea[@name='programDescription']")
    program_price_input = (By.XPATH, "//input[@name='programPrice']")
    sport_dropdown = (By.XPATH, "//select[@name='sport']")
    best_fit_button = (By.XPATH, "//button[contains(text(), 'Best Fit For')]")
    next_button = (By.XPATH, "//button[contains(text(), 'Next')]")

    def create_program(self, title, description, price, sport):
        self.wait.until(EC.element_to_be_clickable(self.programs_tab)).click()
        self.wait.until(EC.visibility_of_element_located(self.program_title_input)).send_keys(title)
        self.wait.until(EC.visibility_of_element_located(self.program_desc_input)).send_keys(description)
        self.wait.until(EC.visibility_of_element_located(self.program_price_input)).send_keys(price)
        # Select sport from dropdown
        sport_select_elem = self.wait.until(EC.visibility_of_element_located(self.sport_dropdown))
        Select(sport_select_elem).select_by_visible_text(sport)
        # Click best fit for button (if there are multiple, adjust as needed)
        self.wait.until(EC.element_to_be_clickable(self.best_fit_button)).click()
        # Click next
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()
        create_button = (By.XPATH, "//button[contains(text(), 'Create')]")
        self.wait.until(EC.element_to_be_clickable(create_button)).click()