from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 💻 הבדיקה מקבלת את ה-driver באופן אוטומטי מה-conftest.py
def test_youtube_search_kdrama(driver):
    # 1. כניסה ליוטיוב
    driver.get("https://www.youtube.com")

    # 2. מציאת תיבת החיפוש לפי ה-NAME
    search_field = driver.find_element(By.NAME, "search_query")

    # 3. הקלדת שם השיר החדש שבחרת (בחירה מעולה, דרך אגב! "The Interest of Love" דרמה מדהימה)
    search_field.clear()  # תמיד טוב לנקות לפני שמקלידים
    search_field.send_keys("LAS Shadow Love")

    # 4. לחיצה על מקש ENTER במקלדת
    search_field.send_keys(Keys.ENTER)

    # 5. בדיקה חכמה שהתוצאות עלו וכותרת העמוד מכילה את שם השיר
    assert "Shadow Love" in driver.title