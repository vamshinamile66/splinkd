# import pytest
# import json
# import time
# from pages.my_team_page import MyTeamPage

# with open("config.json") as f:
#     config = json.load(f)
# team = config["my_team"]
# validations = config["validations"]

# # email-Replace placeholder with dynamic value
# timestamp = int(time.time())
# dynamic_email = f"myteam{timestamp}@otsi.co.in"
# team['email'] = dynamic_email

# @pytest.mark.usefixtures("driver")
# def test_click_on_my_team_tab(driver):
#     page = MyTeamPage(driver)
#     page.click_my_team_tab()

# @pytest.mark.usefixtures("driver")
# def test_click_add_new_team_button(driver):
#     page = MyTeamPage(driver)
#     page.click_create_new_team_button()

# @pytest.mark.usefixtures("driver")
# def test_onboard_my_team_member_with_valid_data(driver):
#     page = MyTeamPage(driver)
#     page.create_first_name(team["first_name"])
#     page.create_last_name(team["last_name"])
#     page.click_and_select_dob(team["month"],team["day"],year=team["year"])
#     page.click_select_gender()
#     page.create_email(team["email"])
#     page.create_mobile(team["mobile"])
#     page.Click_overview_toggle()
#     page.click_save_button()
#     page.toast_message("Successful")

# @pytest.mark.usefixtures("driver")
# def test_existing_email_validation_error(driver):
#     page = MyTeamPage(driver)
#     page.click_my_team_tab()
#     page.click_create_new_team_button()
#     page.create_first_name(team["first_name"])
#     page.create_last_name(team["last_name"])
#     page.click_and_select_dob(team["month"],team["day"],year=team["year"])
#     page.click_select_gender()
#     page.create_email(team["email"])
#     page.create_mobile(team["mobile"])
#     page.Click_overview_toggle()
#     page.click_save_button()
#     page.toast_message("already exists")
#     page.click_cancel_button()

# @pytest.mark.usefixtures("driver")
# def test_mandatory_field_validation_errors(driver):
#     page = MyTeamPage(driver)
#     page.click_create_new_team_button()
#     page.click_save_button()
#     page.validation_messages()
#     time.sleep(1)
#     page.click_cancel_button()
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_Enter_data_for_fields_validation(driver):
#     page = MyTeamPage(driver)
#     page.click_my_team_tab()
#     page.click_create_new_team_button()
#     page.create_first_name(team["first_name"])
#     page.create_last_name(team["last_name"])
#     page.click_and_select_dob(team["month"],team["day"],year=team["year"])
#     page.click_select_gender()
#     page.create_email(validations["static_email"])
#     page.create_mobile(team["mobile"])
#     page.Click_overview_toggle()

# @pytest.mark.usefixtures("driver")
# def test_team_first_name_field_with_minimum_length_validation(driver):
#     page = MyTeamPage(driver)
#     #firt name validation
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(validations["min_value"])
#     page.click_save_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_team_first_name_field_with_maximum_length_validation(driver):
#     page = MyTeamPage(driver)
#     #validate max value
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(validations["max_value"])
#     page.click_save_button()
#     time.sleep(2)
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_team_first_name_field_with_invalid_number_validation(driver):
#     page = MyTeamPage(driver)
#     #numeric value
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(validations["Number"])
#     page.click_save_button()
#     page.validation_messages()

# @pytest.mark.usefixtures("driver")
# def test_team_first_name_field_with_invalid_symbol_validation(driver):
#     page = MyTeamPage(driver)
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(validations["symbol"])
#     page.click_save_button()
#     page.validation_messages()
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(team["first_name"])


# @pytest.mark.usefixtures("driver")
# def test_last_name_field_with_minimum_length_validation(driver):
#     page = MyTeamPage(driver)
#     #firt name validation
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(validations["min_value"])
#     page.click_save_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_last_name_field_with_maximum_length_validation(driver):
#     page = MyTeamPage(driver)
#     #validate max value
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(validations["max_value"])
#     page.click_save_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_last_name_field_with_invalid_number_validation(driver):
#     page = MyTeamPage(driver)
#     #numeric value
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(validations["Number"])
#     page.click_save_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_last_name_field_with_invalid_symbol_validation(driver):
#     page = MyTeamPage(driver)
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(validations["symbol"])
#     page.click_save_button()
#     page.validation_messages()
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(team["last_name"])
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_email_field_with_invalid_email_validation(driver):
#     page = MyTeamPage(driver)
#     #firt name validation
#     page.clear_field(page.email_input)
#     time.sleep(1)
#     page.create_email(validations["invalid_email"])
#     page.click_save_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_email_field_with_invalid_email_number_validation(driver):
#     page = MyTeamPage(driver)
#     #numeric value
#     page.clear_field(page.email_input)
#     time.sleep(1)
#     page.create_email(validations["Number"])
#     page.click_save_button()
#     page.validation_messages()
#     page.clear_field(page.email_input)
#     time.sleep(1)
#     page.create_email(validations["static_email"])
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_mobile_number_field_with_number_less_than_10_digits_validation(driver):
#     page = MyTeamPage(driver)
#     #firt name validation
#     page.clear_field(page.mobile_input)
#     time.sleep(1)
#     page.create_mobile(validations["invalid_mobile_less9"])
#     page.click_save_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_mobile_with_invalid_mobile_text_validation(driver):
#     page = MyTeamPage(driver)
#     #validate max value
#     page.clear_field(page.mobile_input)
#     time.sleep(1)
#     page.create_mobile(validations["invalid_mobile_text"])
#     page.click_save_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_mobile_field_with_invalid_mobile_starting_zero_validation(driver):
#     page = MyTeamPage(driver)
#     #numeric value
#     page.clear_field(page.mobile_input)
#     time.sleep(1)
#     page.create_mobile(validations["invalid_mobile_zero"])
#     page.click_save_button()
#     page.validation_messages()
#     page.clear_field(page.mobile_input)
#     time.sleep(1)
#     page.create_mobile(team["mobile"])
#     page.click_cancel_button()
#     time.sleep(1)


# @pytest.mark.usefixtures("driver")
# #Academy signout
# def test_logout(driver):
#     page = MyTeamPage(driver)
#     page.logout()

# @pytest.mark.usefixtures("driver")
# def test_validating_newly_created_team_member_able_to_signup(driver):
#     driver.get(config["base_url"])
#     page = MyTeamPage(driver)
#     page.signup_team(
#         email=team["email"],
#         password=team["password"],
#         confirm_password=team["confirm_password"],
#         captch_url= config["captch_url"]
#     )


  







import pytest
import json
import time
import random
from pages.my_team_page import MyTeamPage

# Load config data
with open("config.json") as f:
    config = json.load(f)
team = config["my_team"]

def generate_team_members(count=50):
    """
    Generate a list of team member dicts with unique email & mobile.
    """
    members = []
    timestamp = int(time.time())
    for i in range(count):
        dynamic_email = f"myteam{timestamp}{i}@otsi.co.in"
        dynamic_mobile = f"9{random.randint(100000000, 999999999)}"  # 10-digit mobile

        # First/Last name: only letters + numbers allowed (no underscore)
        first_name = f"sanjay{i}"   # ✅ valid: sanjay0, sanjay1, ...
        last_name = f"damu{i}"      # ✅ valid: damu0, damu1, ...

        members.append({
            "first_name": first_name,
            "last_name": last_name,
            "month": team["month"],
            "day": team["day"],
            "year": team["year"],
            "email": dynamic_email,
            "mobile": dynamic_mobile
        })
    return members

# Generate 50 members for testing
members_list = generate_team_members(50)


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("member", members_list)
def test_onboard_multiple_team_members(driver, member):
    page = MyTeamPage(driver)
    page.click_my_team_tab()
    page.click_create_new_team_button()
    page.create_first_name(member["first_name"])
    page.create_last_name(member["last_name"])
    page.click_and_select_dob(member["month"], member["day"], year=member["year"])
    page.click_select_gender()
    page.create_email(member["email"])
    page.create_mobile(member["mobile"])
    page.Click_overview_toggle()
    page.click_save_button()
    page.toast_message("Successful")
    time.sleep(1)  
















    


    


