import time
from selenium.webdriver.common.by import By


# 1. בדיקה חיובית: בדיקת תקינות קישור הסטרימינג
def test_streaming_link_properties(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")
    link_element = driver.find_element(By.ID, "streaming-link")
    assert "ateamas.com" in link_element.get_attribute("href")
    assert link_element.get_attribute("target") == "_blank"


# 2. בדיקה שלילית: מניעת הוספת דרמה שכבר קיימת ברשימה
def test_prevent_duplicate_drama(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")
    input_field = driver.find_element(By.ID, "new-drama-input")
    input_field.clear()
    input_field.send_keys("Goblin")
    driver.find_element(By.ID, "add-drama-btn").click()
    time.sleep(1)

    # 🌟 התיקון החדש: מאתרים את ה-Alert, מוודאים את הטקסט שלו ומאשרים (סוגרים) אותו!
    alert = driver.switch_to.alert
    assert "כבר קיימת ברשימה" in alert.text
    alert.accept()  # סגירת החלון הקופץ כדי שסלניום יוכל להמשיך בדף
    time.sleep(0.5)

    # עכשיו כשהמסך פנוי, סלניום יכול לספור את הסדרות בבטחה
    dramas = driver.find_elements(By.CLASS_NAME, "drama-name")
    assert len(dramas) == 1


# 3. בדיקה שלילית: ולידציה שהמערכת חוסמת סדרות מומצאות ומקפיצה Alert
def test_fake_drama_error_alert(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")
    input_field = driver.find_element(By.ID, "new-drama-input")
    input_field.clear()
    input_field.send_keys("Fake Drama 123")
    driver.find_element(By.ID, "add-drama-btn").click()
    time.sleep(1)

    alert = driver.switch_to.alert
    assert "בחלום הליל" in alert.text
    alert.accept()

    dramas = driver.find_elements(By.CLASS_NAME, "drama-name")
    assert "Fake Drama 123" not in [d.text for d in dramas]


# 🟢 4. בדיקה חיובית: מחיקת סדרה מהרשימה ("מחק, איכסה של סדרה")
def test_delete_drama_from_list(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")

    dramas = driver.find_elements(By.CLASS_NAME, "drama-name")
    assert len(dramas) == 1

    # איתור כפתור המחיקה החדש
    delete_button = driver.find_element(By.CLASS_NAME, "delete-btn")
    assert delete_button.text == "מחק, איכסה של סדרה"  # ולידציה לטקסט החדש!

    delete_button.click()
    time.sleep(1)

    dramas_after_delete = driver.find_elements(By.CLASS_NAME, "drama-name")
    assert len(dramas_after_delete) == 0


# 🟢 5. בדיקה חיובית: סימון סדרה כ"נצפה"
def test_mark_drama_as_watched(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")

    watch_button = driver.find_element(By.CLASS_NAME, "watch-btn")
    watch_button.click()
    time.sleep(1)

    assert watch_button.text == "ראיתי! ✓"


# 🟢 6. בדיקה חיובית: בדיקת שמירת מיקום צפייה (פרק ודקה)
def test_save_watching_progress(driver):
    driver.get("file:///C:/programming/learn to code/pycharm/workspace/PythonProject7/kdrama_site.html")

    # 1. נלחץ על כפתור "איפה עצרתי? ⏱️" כדי לפתוח את פאנל ההזנה
    track_button = driver.find_element(By.CLASS_NAME, "track-btn")
    track_button.click()
    time.sleep(0.5)

    # 2. נאתר את שדה הטקסט החדש ונזין מיקום
    progress_input = driver.find_element(By.CLASS_NAME, "track-input")
    progress_input.clear()
    progress_input.send_keys("פרק 5 דקה 15")

    # 3. נלחץ על כפתור השמירה
    save_button = driver.find_element(By.CLASS_NAME, "save-track-btn")
    save_button.click()
    time.sleep(1)

    # 4. נוודא שהטקסט אכן התעדכן על המסך
    status_msg = driver.find_element(By.CLASS_NAME, "saved-status")
    assert status_msg.text == "נשמר: פרק 5 דקה 15"
