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

def test_login(setup_driver):
    driver = setup_driver
    try:
        # Открываем главную страницу тестируемого сайта
        driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
        
        # Находим и нажимаем кнопку "Логин"
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Логин"))
        )
        login_link.click()
        
        # Вводим данные для входа
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_input.send_keys("qwerty123@gmail.com")
        
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("qwerty123")
        
        # Нажимаем кнопку "Войти"
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Ожидаем появления сообщения о успешном входе
        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-message"))
        ).text
        
        # Проверяем, что сообщение соответствует ожидаемому результату
        assert message == "Пользователь вошел в систему", f"Ожидалось 'Пользователь вошел в систему', получено '{message}'"
        print(message)
    
    finally:
        time.sleep(3)
