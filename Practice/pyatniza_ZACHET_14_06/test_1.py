import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def setup_driver():
   
    driver = webdriver.Chrome()
    yield driver #приостанавливает выполнение функции(return останавливает совсем)
    driver.quit()  

def test_registration(setup_driver):
    driver = setup_driver
    try:
        # Открываем главную страницу тестируемого сайта
        driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
        
        # Находим и нажимаем кнопку "Регистрация"
        registration_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Регистрация"))
        )
        registration_link.click()
        
        # Ожидаем появления поля для ввода имени, затем вводим произвольные данные
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        )
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")
        
        name_input.send_keys("Galina")
        email_input.send_keys("qwerty123@example.com")
        password_input.send_keys("qwerty123")
        
        # Нажимаем кнопку "Зарегистрироваться"
        register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()
        
        # Ожидаем появления сообщения о успешной регистрации
        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "register-message"))
        ).text
        
        # Проверяем, что сообщение соответствует ожидаемому результату
        assert message == "Пользователь зарегистрирован", f"Ожидалось 'Пользователь зарегистрирован', получено '{message}'"
        print(message)
    
    finally:

        time.sleep(3)