import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def test_youtube_search_kdrama():
    # 1. פתיחת הדפדפן
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # 2. כניסה ליוטיוב
    driver.get("https://www.youtube.com")
    driver.maximize_window()

    # 3. מציאת תיבת החיפוש לפי ה-NAME שגילינו עבור יוטיוב
    search_field = driver.find_element(By.NAME, "search_query")

    # 4. הקלדת שם השיר
    search_field.send_keys("Stay With Me Goblin OST")

    # 5. לחיצה על מקש ENTER במקלדת
    search_field.send_keys(Keys.ENTER)

    # הפסקה קלה של 3 שניות כדי לראות את התוצאות
    time.sleep(3)

    # 6. בדיקה שהגענו לדף התוצאות והמילה Goblin מופיעה בתוך ה-URL
    assert "Goblin" in driver.current_url

    # 7. סגירת הדפדפן
    driver.quit()