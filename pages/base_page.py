import re
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- Common reusable methods ----------
    def normalize_error(self, text: str) -> str:
        """Normalize validation message text (lowercase, strip punctuation/spaces)."""
        return re.sub(r'[^a-z]', '', text.lower())
#------------disabled the code because stale element exception------------------------------
    # def validations_capture(self):
    #     """
    #     Collects validation errors from form.
    #     Returns dictionary: {field_label: normalized_error_message}
    #     """
    #     errors = {}
    #     error_elements = self.driver.find_elements(By.CSS_SELECTOR, "p.text-destructive")

    #     if error_elements:
    #         print("Mandatory field validations are captured:")

    #     for elem in error_elements:
    #         error_text = elem.text.strip()
    #         if not error_text:
    #             continue

    #         # Try to find label/input linked with the error
    #         field_name = "Unknown field"
    #         try:
    #             label_elem = elem.find_element(By.XPATH, "./preceding::label[1]")
    #             field_name = label_elem.text.strip()
    #         except:
    #             try:
    #                 input_elem = elem.find_element(By.XPATH, "./preceding::input[1]")
    #                 field_name = input_elem.get_attribute("placeholder") or "Unknown field"
    #             except:
    #                 pass

    #         # Clean field name
    #         field_name = field_name.replace("\n", " ").replace("*", "").strip()

    #         # Normalize error message
    #         normalized = self.normalize_error(error_text)
    #         errors[field_name] = normalized

    #         print(f"{field_name}: {error_text}")

    #     return errors
#-------------------------------------------


    def validations_capture(self):
            """
            Collects validation errors from form.
            Returns dictionary: {field_label: normalized_error_message}
            """
            errors = {}
            error_selectors = (By.CSS_SELECTOR, "p.text-destructive")

            error_elements = self.driver.find_elements(*error_selectors)

            if error_elements:
                print("Mandatory field validations are captured:")

            for elem in error_elements:
                try:
                    error_text = elem.text.strip()
                    if not error_text:
                        continue

                    # Try to find label/input linked with the error
                    field_name = "Unknown field"
                    try:
                        label_elem = elem.find_element(By.XPATH, "./preceding::label[1]")
                        field_name = label_elem.text.strip()
                    except Exception:
                        try:
                            input_elem = elem.find_element(By.XPATH, "./preceding::input[1]")
                            field_name = input_elem.get_attribute("placeholder") or "Unknown field"
                        except Exception:
                            pass

                    # Clean field name
                    field_name = field_name.replace("\n", " ").replace("*", "").strip()

                    # Normalize error message
                    normalized = self.normalize_error(error_text)
                    errors[field_name] = normalized

                    print(f"{field_name}: {error_text}")

                except StaleElementReferenceException:
                    print("⚠️ Skipped a stale error element (DOM refreshed).")
                    continue

            return errors
    def compare_errors(self, expected_errors: dict, actual_errors: dict) -> bool:
        """
        Compare expected vs actual validation errors.
        Normalizes both before comparison.
        Returns True if all expected errors match actual errors.
        """
        norm_expected = {k.lower(): self.normalize_error(v) for k, v in expected_errors.items()}
        norm_actual = {k.lower(): v for k, v in actual_errors.items()}

        all_matched = True
        for field, expected_msg in norm_expected.items():
            actual_msg = norm_actual.get(field)
            if actual_msg != expected_msg:
                print(f"❌ Mismatch for '{field}' → Expected: {expected_msg}, Got: {actual_msg}")
                all_matched = False
            else:
                print(f"✅ '{field}' matched → {expected_msg}")

        return all_matched
    def clear_field(self, locator):
        """Clear input field."""
        field = self.wait.until(EC.presence_of_element_located(locator))
        field.clear()

    def toast_message(self, message, timeout=10):
        """Capture toast/flash message by text content."""
        try:
            toast = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{message}')]"))
            )
            print("Toast appeared:", toast.text)
            return toast.text
        except Exception as e:
            print(f"Error: {str(e)}")
            return None
        
    # this methode uing for forgot password based on title & description
    def get_toast_message(self, timeout=10):
        """Wait for toast/flash message and return (title, description)."""
        try:
            wait = WebDriverWait(self.driver, timeout)

            # Wait for toast container (success message)
            toast = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "li[data-sonner-toast][data-type='success']")
            ))

            # Extract title and description
            title = toast.find_element(By.CSS_SELECTOR, "div[data-title]").text
            self.driver.save_screenshot("toast_missing1.png")
            try:
                desc = toast.find_element(By.CSS_SELECTOR, "div[data-description]").text
            except:
                self.driver.save_screenshot("toast_missing.png")
                desc = ""

            print(f"✅ Toast captured: {title} - {desc}")
            return title, desc

        except Exception as e:
            print(f"❌ Toast not found: {str(e)}")
            self.driver.save_screenshot("toast_not_found.png")  # Debugging
            return None, None



   

    def logout(self):
        """Perform logout if toggle + signout available."""
        try:
            toggle_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/span"))
            )
            toggle_button.click()
            time.sleep(2)

            signout_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign Out')]"))
            )
            signout_button.click()
        except Exception as e:
            print(f"Error during sign out: {e}")
