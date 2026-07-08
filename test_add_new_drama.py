from selenium.webdriver.common.by import By

def test_add_custom_drama(driver):
    # 1. ניווט לקובץ ה-HTML המקומי שלך
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")

    # 2. מציאת שדה הטקסט, ניקוי שלו והקלדת שם הדרמה החדשה
    input_field = driver.find_element(By.ID, "new-drama-input")
    input_field.clear()
    input_field.send_keys("My Roommate Is a Gumiho")

    # 3. מציאת כפתור ההוספה הכחול ולחיצה עליו
    add_button = driver.find_element(By.ID, "add-drama-btn")
    add_button.click()

    # 4. מציאת הרשימה ובדיקה שהסדרה החדשה אכן התווספה אליה בהצלחה!
    drama_list = driver.find_element(By.ID, "drama-list")
    assert "My Roommate Is a Gumiho" in drama_list.text