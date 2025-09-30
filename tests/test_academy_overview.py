
import pytest
from pages.academy_overview_page import AcademyOverviewPage

@pytest.mark.usefixtures("driver")
def test_click_on_coaches_tab(driver):
    page = AcademyOverviewPage(driver)
    page.click_coaches_tab()

@pytest.mark.usefixtures("driver")
def test_get_coaches_count(driver):
    page = AcademyOverviewPage(driver)
    #coach count in coaches tab
    coach_names = page.get_coach_names()
    print(f"\n👨‍🏫 Coach count in coaches Tab : {len(coach_names)}")
    coachTab_coach_count= page.coachTab_count_coaches()
    print(f"\n👨‍🏫 Coach count in coaches Tab using count function : {coachTab_coach_count}")
    assert len(coach_names) > 0, "No coaches found"

@pytest.mark.usefixtures("driver")
def test_click_on_overview_tab(driver):
    page = AcademyOverviewPage(driver)
    #coaches count in overview tab
    page.click_Overview_tab()
@pytest.mark.usefixtures("driver")
def test_capture_coach_count_in_overview_tab(driver):
    page = AcademyOverviewPage(driver)
    overview_coach_count = page.get_overview_coach_count()
    print(f"\n👨‍🏫 Total Coaches in Overview Page: {overview_coach_count}")
    page.get_overview_coach_count()

@pytest.mark.usefixtures("driver")
def test_compare_coach_count_is_same_displayed_in_overview_and_coach_tab(driver):
    page = AcademyOverviewPage(driver)
    # Get coaches count in coaches tab
    coachTab_coach_count = page.coachTab_count_coaches()
    # Get coaches count in overview tab
    overview_coach_count = page.get_overview_coach_count()
    # Compare coaches count in overview and coaches tab
    assert coachTab_coach_count == overview_coach_count, (
        f"❌ Mismatch! Overview: {overview_coach_count}, Coaches Tab: {coachTab_coach_count}"
    )
    print("✅ Test Passed! Coaches Count match.")