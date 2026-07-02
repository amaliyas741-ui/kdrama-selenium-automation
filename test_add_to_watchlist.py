from selenium.webdriver.common.by import By


def test_add_to_watchlist(driver):
    driver.get(r"file:///C:\programming\learn to code\pycharm\workspace\PythonProject7\kdrama_site.html")
    button = driver.find_element(By.ID, "watchlist-btn")

    assert "הוסף לרשימת הצפייה" in button.text
    button.click()
    assert "התווסף לרשימה" in button.text