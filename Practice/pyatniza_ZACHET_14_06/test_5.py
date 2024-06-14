import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_dynamic_content_page(driver):
    driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
    
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Динамический контент"))
    )
    button.click()
    time.sleep(2)

def test_add_element(open_dynamic_content_page, driver):
    add_button = driver.find_element(By.ID, "add-element")
    assert add_button is not None, "Кнопка 'Добавить элемент' не найдена"
    
    add_button.click()
    time.sleep(2)
    
    new_element = driver.find_element(By.XPATH, "//*[text()='Новый элемент']")
    assert new_element is not None, "Новый элемент не был добавлен"
    
    message = driver.find_element(By.ID, "content-area").text
    assert message == "Элемент добавлен", f"Ожидалось сообщение 'Элемент добавлен', но '{message}'"
    print(message)