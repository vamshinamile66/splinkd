from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class CoachPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def onboard_coach(self, first_name, last_name, dob, gender, email, mobile):
        # 1. Click on coaches tab
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Coaches')]"))).click()
        # 2. Click on 'on board coaches' button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'On Board Coaches')]"))).click()
        # 3. Enter first name
        self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
        # 4. Enter last name
        self.wait.until(EC.visibility_of_element_located((By.NAME, "lastName"))).send_keys(last_name)
        # 5. Select date of birth
        self.wait.until(EC.visibility_of_element_located((By.NAME, "dob"))).send_keys(dob)
        # 6. Select gender dropdown
        Select(self.wait.until(EC.visibility_of_element_located((By.NAME, "gender")))).select_by_visible_text(gender)
        # 7. Enter email
        self.wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)
        # 8. Enter mobile number
        self.wait.until(EC.visibility_of_element_located((By.NAME, "mobile"))).send_keys(mobile)
        # 9. Click on create button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create')]"))).click()