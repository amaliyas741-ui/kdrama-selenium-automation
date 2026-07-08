import time  # 🌟 הוספנו את זה למעלה כדי לאפשר השהיות
from selenium.webdriver.common.by import By

# 🟢 1. הבדיקה החיובית: מוודאת שדרמה חדשה מתווספת לרשימה בהצלחה
def test_add_custom_drama(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")

    input_field = driver.find_element(By.ID, "new-drama-input")
    input_field.clear()
    input_field.send_keys("My Roommate Is a Gumiho")

    add_button = driver.find_element(By.ID, "add-drama-btn")
    add_button.click()

    time.sleep(1)  # 🌟 נותנים לדפדפן שנייה אחת לעכל את ההוספה והעיצוב החדש

    drama_list = driver.find_element(By.ID, "drama-list")
    assert "My Roommate Is a Gumiho" in drama_list.text


# 🔴 2. הבדיקה השלילית: מוודאת שלחיצה על ריק לא מוסיפה שום דבר
def test_add_empty_drama_error(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")

    input_field = driver.find_element(By.ID, "new-drama-input")
    input_field.clear()

    add_button = driver.find_element(By.ID, "add-drama-btn")
    add_button.click()

    drama_list = driver.find_element(By.ID, "drama-list")

    # מוודאים שגובלין שם, ושהטקסט המדויק של הרשימה נשאר רק "Goblin" בלי תוספות ריקות
    assert "Goblin" in drama_list.text
    assert drama_list.text.strip() == "Goblin"