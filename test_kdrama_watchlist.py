import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # ספרייה שמאפשרת ללחוץ על מקשים כמו ENTER
from webdriver_manager.chrome import ChromeDriverManager


def test_google_search_kdrama():
    # 1. פתיחת הדפדפן
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # 2. כניסה לגוגל
    driver.get("https://www.google.com")
    driver.maximize_window()

    # 3. מציאת תיבת החיפוש לפי ה-ID החדש שגילינו ב-F12
    search_field = driver.find_element(By.ID, "APjFqb")

    # 4. הקלדת שם הדרמה האהובה עלייך
    search_field.send_keys("Squid Game")

    # 5. לחיצה על מקש ENTER במקלדת כדי לבצע את החיפוש
    search_field.send_keys(Keys.ENTER)

    # הפסקה קלה של 3 שניות כדי שתוכלי לראות את תוצאות החיפוש בעיניים
    time.sleep(3)

    # 6. בדיקה (Assert) שתוצאות החיפוש אכן קשורות לסדרה (הטקסט מופיע בכותרת הטאב)
    # 6. בדיקה שהגענו לדף התוצאות ע"י בדיקה שהמילה Squid מופיעה ב-URL
    assert "Squid" in driver.current_url

    # 7. סגירת הדפדפן
    driver.quit()