import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_registration_form(setup_driver):
    driver = setup_driver
    driver.get("https://erikdark.github.io/QA_DIPLOM/")  

    # Находим и нажимаем "Регистрация"
    registration_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Регистрация"))
    )
    registration_link.click()

def is_valid_name(name):
    return bool(re.match(r'^[A-Za-z\-]+$', name))

def is_valid_email(email):
    return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))

def is_valid_password(password):
    return (len(password) >= 8 and 
            re.search(r'[A-Z]', password) and 
            re.search(r'[a-z]', password) and 
            re.search(r'[0-9]', password))

def test_registration_validation(setup_driver, open_registration_form):
    driver = setup_driver

    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "confirmPassword")
    register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Правильные данные
    valid_data = {
        "name": "Galina-Galina",
        "email": "qwerty123@example.com",
        "password": "Q*WErty45@exemple.com",
        "confirm_password": "Q*WErty45@exemple.com"
    }

    # Заполняем поля 
    name_input.send_keys(valid_data["name"])
    email_input.send_keys(valid_data["email"])
    password_input.send_keys(valid_data["password"])
    confirm_password_input.send_keys(valid_data["confirm_password"])
    register_button.click()

    # Ожидаем сообщения о регистрации 
    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "register-message"))
    ).text

    assert message == "Пользователь зарегистрирован", f"Ожидалось 'Пользователь зарегистрирован', получено '{message}'"

    # Тест некор варианты
    invalid_data = [
        {"name": "Galina123", "email": "qwerty123@example.com", "password": "Q*WErty45@exemple.com", "confirm_password": "Q*WErty45@exemple.com", "error_field": "name"},
        {"name": "Galina-Galina", "email": "qwerty123@com", "password": "Q*WErty45@exemple.com", "confirm_password": "Q*WErty45@exemple.com", "error_field": "email"},
        {"name": "Galina-Galina", "email": "qwerty123@example.com", "password": "pass", "confirm_password": "pass", "error_field": "password"},
        {"name": "Galina-Galina", "email": "qwerty123@example.com", "password": "Q*WErty45@exemple.com", "confirm_password": "Q*WErty45@exemple2.com", "error_field": "confirm_password"}
    ]

    for data in invalid_data:
        # Очищаем поля формы
        name_input.clear()
        email_input.clear()
        password_input.clear()
        confirm_password_input.clear()

        # некор данные
        name_input.send_keys(data["name"])
        email_input.send_keys(data["email"])
        password_input.send_keys(data["password"])
        confirm_password_input.send_keys(data["confirm_password"])
        register_button.click()

        # проверяем ошибки
        if data["error_field"] == "name" and not is_valid_name(data["name"]):
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "name-error"))
            ).text
            assert "Имя должно содержать только буквы и символ '-'" in error_message

        if data["error_field"] == "email" and not is_valid_email(data["email"]):
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "email-error"))
            ).text
            assert "Некорректный формат email" in error_message

        if data["error_field"] == "password" and not is_valid_password(data["password"]):
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "password-error"))
            ).text
            assert "Пароль должен содержать не менее 8 символов, включая одну заглавную букву, одну строчную букву и одну цифру" in error_message

        if data["error_field"] == "confirm_password" and data["password"] != data["confirm_password"]:
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "confirm-password-error"))
            ).text
            assert "Пароли не совпадают" in error_message