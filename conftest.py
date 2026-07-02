import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=service)
    _driver.maximize_window()
    _driver.implicitly_wait(10)

    yield _driver

    _driver.quit()