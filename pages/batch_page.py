from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class BatchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_batch(self, program_name, batch_name, start_hour, start_minute, end_hour, end_minute):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{program_name}']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Batch')]"))).click()
        self.wait.until(EC.visibility_of_element_located((By.NAME, "batchName"))).send_keys(batch_name)
        Select(self.wait.until(EC.visibility_of_element_located((By.NAME, "start_hour")))).select_by_visible_text(start_hour)
        Select(self.wait.until(EC.visibility_of_element_located((By.NAME, "start_minute")))).select_by_visible_text(start_minute)
        Select(self.wait.until(EC.visibility_of_element_located((By.NAME, "end_hour")))).select_by_visible_text(end_hour)
        Select(self.wait.until(EC.visibility_of_element_located((By.NAME, "end_minute")))).select_by_visible_text(end_minute)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save')]"))).click()
        success_elem = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
        print("Batch creation success message:", success_elem.text)

    def check_mandatory_field_errors(self, program_name):
        # Click on created program name
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{program_name}']"))).click()
        # Click on 'add batch'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Batch')]"))).click()
        # Do NOT fill any fields, just click save
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save')]"))).click()
        # Collect error messages
        error_elements = self.driver.find_elements(By.CLASS_NAME, "invalid-feedback")
        if not error_elements:
            error_elements = self.driver.find_elements(By.CSS_SELECTOR, ".error-message, .text-danger, .alert-danger")
        return [elem.text for elem in error_elements if elem.text.strip()]