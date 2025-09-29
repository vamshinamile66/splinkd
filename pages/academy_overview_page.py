        
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AcademyOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Tabs
    OVERVIEW_TAB = (By.XPATH, "//button[span[text()='Overview']]")
    COACHES_TAB = (By.XPATH, "//button[.//span[normalize-space(text())='Coaches']]")
   

    # Coach name (ONLY the h3 in the card header)
    COACH_NAME_H3 = (By.XPATH, "//div[@data-slot='card-header']//h3")
    overview_COACH_COUNT = (By.XPATH, "//div[text()='Coaches']/following::h3[@class='font-semibold'][1]")
    overview_ATHLETES_COUNT = (By.XPATH, "//div[text()='Athletes']/following::h3[@class='font-semibold'][1]")
    overview_active_program_count=(By.XPATH, "//div[text()='Active Programs']/following::h3[@class='font-semibold'][1]")
    
    #overview tab data
    def click_Overview_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.OVERVIEW_TAB)).click()
        print("Clicked on Overview tab")
    def get_overview_coach_count(self):
        elem = self.wait.until(EC.presence_of_element_located(self.overview_COACH_COUNT))
        return int(elem.text.strip())
    def get_overview_athletes_count(self):
        # Capture Athletes count
        elem = self.wait.until(EC.presence_of_element_located(self.overview_ATHLETES_COUNT))
        print("Athletes Count:",elem.text.strip())
        return int(elem.text.strip())
    def get_programs_count(self):  
        elem = self.wait.until(EC.presence_of_element_located(self.overview_active_program_count))
        print("Athletes Count:",elem.text.strip())
        return int(elem.text.strip())
    
    #coach tab data
    def click_coaches_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.COACHES_TAB)).click()
        print("Clicked on Coaches tab")

    def _coach_name_elements(self):
        # wait for at least one card to appear
        self.wait.until(EC.presence_of_all_elements_located(self.COACH_NAME_H3))
        elems = self.driver.find_elements(*self.COACH_NAME_H3)
        # keep only visible ones (avoids hidden templates)
        return [e for e in elems if e.is_displayed() and e.text.strip()]

    def get_coach_names(self):
        names = []
        for el in self._coach_name_elements():
            try:
                names.append(el.text.strip())
            except Exception:
                # if a stale element occurs, just skip it; we only need text
                continue
        return names

    def coachTab_count_coaches(self):
        return len(self._coach_name_elements())
