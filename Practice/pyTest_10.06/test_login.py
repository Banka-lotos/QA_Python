import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_successful(browser):
    browser.get("https://erikdark.github.io/Qa_autotests_reg_form_pop_up/")
    username_input = browser.find_element(By.ID, "username")
    password_input = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.XPATH, "//button[text()='Login']")

    # Вводим логин и пароль
    username_input.send_keys("testuser")
    password_input.send_keys("password123")

    # Нажимаем кнопку "Login"
    login_button.click()

    # Ждем закрытия модального окна
    WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, "loginModal")))

    # Проверяем, что модальное окно успешно закрылось
    assert not browser.find_elements(By.ID, "loginModal")

def test_login_failed_wrong_credentials(browser):
    browser.get("https://erikdark.github.io/Qa_autotests_reg_form_pop_up/")
    username_input = browser.find_element(By.ID, "username")
    password_input = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.XPATH, "//button[text()='Login']")

    # Вводим неправильные логин и пароль
    username_input.send_keys("invaliduser")
    password_input.send_keys("invalidpassword")

    # Нажимаем кнопку "Login"
    login_button.click()

    # Проверяем наличие сообщения об ошибке
    error_message = browser.find_element(By.ID, "errorMessage")
    assert error_message.text == "Invalid username or password."

def test_login_failed_no_credentials(browser):
    browser.get("https://erikdark.github.io/Qa_autotests_reg_form_pop_up/")
    login_button = browser.find_element(By.XPATH, "//button[text()='Login']")

    # Нажимаем кнопку "Login" без ввода логина и пароля
    login_button.click()

    # Проверяем наличие сообщения об ошибке
    error_message = browser.find_element(By.ID, "errorMessage")
    assert error_message.text == "Please enter username and password."
    