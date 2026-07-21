import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.visual_comparator import compare_images


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # הרצה ללא דפדפן פיזי עבור CI/CD
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_homepage_ui_and_visual(driver):
    """בדיקת UI עם Selenium בתוספת בדיקה ויזואלית"""
    driver.get("https://example.com")  # החליפי בכתובת האתר שלך

    # 1. בדיקת UI בסיסית
    title = driver.title
    assert "Example" in title, "כותרת האתר אינה תואמת"

    # 2. בדיקה ויזואלית (Visual Testing)
    actual_screenshot = "actual_screenshot.png"
    baseline_screenshot = "baseline_screenshot.png"
    diff_screenshot = "diff_screenshot.png"

    driver.save_screenshot(actual_screenshot)

    # אם אין תמונת ייחוס (Baseline), נשמור אותה ראשונה
    if not os.path.exists(baseline_screenshot):
        driver.save_screenshot(baseline_screenshot)
        print("📸 תמונת Baseline נוצרה בהצלחה.")
    else:
        is_identical = compare_images(baseline_screenshot, actual_screenshot, diff_screenshot)
        assert is_identical, "❌ נמצאה סטייה ויזואלית! בדוק את diff_screenshot.png"