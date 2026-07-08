import time
from selenium.webdriver.common.by import By  # 🌟 השורה הזו פותרת את השגיאה!

def test_add_empty_drama_error(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")

    input_field = driver.find_element(By.ID, "new-drama-input")
    input_field.clear()

    add_button = driver.find_element(By.ID, "add-drama-btn")
    add_button.click()

    drama_list = driver.find_element(By.ID, "drama-list")

    # מוודאים שגובלין שם
    assert "Goblin" in drama_list.text

    # 🌟 התיקון החדש שלך כאן:
    # מוודאים שהרשימה עדיין מכילה רק פריט אחד ולא התווספה שורה ריקה
    all_items = drama_list.find_elements(By.TAG_NAME, "li")
    assert len(all_items) == 1