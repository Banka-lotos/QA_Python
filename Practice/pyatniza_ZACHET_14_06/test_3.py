import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome()
    yield driver  #приостанавливает выполнение функции(return останавливает совсем)
    driver.quit()

def test_logout_from_profile(setup_driver):
    driver = setup_driver
   
    driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
    
    # Находим и нажимаем кнопку "Профиль"
    profile_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Профиль"))
    )
    profile_link.click()
    

    # Находим и кликаем на кнопку "Выход"
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout-button"))
    )
    logout_button.click()
    
    # Ожидаем сообщения о успешном выходе
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logout-message"))
    ).text
    
    # Проверяем, что сообщение соответствует ожидаемому результату
    assert message == "Пользователь вышел из системы", f"Ожидалось 'Пользователь вышел из системы', получено '{message}'"
    print(message)
    
    time.sleep(3) 