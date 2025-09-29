from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SchedulesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    SCHEDULES_TAB = (By.XPATH, "//span[normalize-space()='Schedules']")

    # Actions
    def click_schedules_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.SCHEDULES_TAB)).click()
        print("✅ Schedules tab clicked")

    def verify_view_options_displayed(self):
        """Check Day/Month/Year/Agenda buttons are visible"""
        labels = ["View by day", "View by month", "View by year", "View by agenda"]

        for label in labels:
            element = self.driver.find_element(By.XPATH, f"//span[@aria-label='{label}']")
            assert element.is_displayed(), f"{label} button not visible"
        print("✅ View options Day/Month/Year/Agenda are visible")

    

    # def get_programs_by_date(self, date_text):
    #  try:
    #     # Locate the date section
    #     date_section = self.wait.until(
    #         EC.presence_of_element_located((By.XPATH, f"//p[contains(text(),'{date_text}')]"))
    #     )

    #     # Fetch all programs under that date
    #     programs = date_section.find_elements(
    #         By.XPATH,
    #         "./following-sibling::div//div[contains(@class,'text-sm') and contains(@class,'font-medium')]"
    #     )

    #     program_list = [p.text for p in programs]
    #     # print(f"📅 Programs under {date_text}:")
    #     for prog in program_list:
    #         print(f"   - {prog}")

    #     return program_list

    #  except Exception as e:
    #     print(f"❌ Error while fetching programs: {e}")
    #     return []

    def find_program_and_coach(self, title):
    
     try:
        # Get all program blocks (each has program + coach together)
        blocks = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'space-y-1')]"))
        )

        for block in blocks:
            try:
                program = block.find_element(By.XPATH, ".//div[contains(@class,'text-sm') and contains(@class,'font-medium')]")
                coach = block.find_element(By.XPATH, ".//div[contains(@class,'leading-none')]")

                if title.lower() in program.text.lower():
                    return program.text, coach.text

            except Exception:
                continue

        print(f"❌ Program '{title}' not found")
        return None, None
     except Exception as e:
        print(f"❌ Error while searching: {e}")
        return None, None

        
   
