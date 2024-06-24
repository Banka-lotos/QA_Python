import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_registration_form(setup_driver):
    driver = setup_driver
    driver.get("https://erikdark.github.io/QA_DIPLOM/")
    
    # Нажимаем на ссылку "Регистрация"
    registration_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Регистрация"))
    )
    registration_link.click()

def test_registration_validation(setup_driver, open_registration_form):
    driver = setup_driver

    # Заполняем форму регистрации
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "confirmPassword")
    register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    name_input.send_keys("Galina-Galina")
    email_input.send_keys("qwerty123@example.com")
    password_input.send_keys("Q*WErty45@exemple.com")
    confirm_password_input.send_keys("Q*WErty45@exemple.com")
    register_button.click()

    # Ожидаем сообщения о регистрации
    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "register-message"))
    ).text

    assert message == "Пользователь зарегистрирован", f"Ожидалось 'Пользователь зарегистрирован', получено '{message}'"
    print(message)