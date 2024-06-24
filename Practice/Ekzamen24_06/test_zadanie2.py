import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_login_form(setup_driver):
    driver = setup_driver
    driver.get("https://erikdark.github.io/QA_DIPLOM/")
    
    vhod_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Вход"))
    )
    vhod_link.click()
    
    return driver

def test_add_and_validate_users(open_login_form):
    driver = open_login_form

    users = [
        {"login": "Lev-lev", "password": "Qwe$457"},
        {"login": "Bob-Bob", "password": "Qwe$45*"},
        {"login": "Bob-Bob", "password": "Qwe$757"},
        {"login": "Fan-Fan", "password": "Qwe$453"},
        {"login": "Mem-Mem", "password": "Qwe$456"},
        {"login": "MENYA", "password": "Qwer12*4"},
        {"login": "YZHE", "password": "Qwer12*SD"},
        {"login": "BESIT", "password": "Pa87r12KL"},
        {"login": "newuser", "password": "NewPaswr1234"}
    ]

    for user in users:
        # Добавляем нового пользователя
        new_login_input = driver.find_element(By.ID, "newLogin")
        new_password_input = driver.find_element(By.ID, "newPassword")
        add_button = driver.find_element(By.CSS_SELECTOR, "form#addUserForm button[type='submit']")

        new_login_input.clear()
        new_login_input.send_keys(user["login"])
        new_password_input.clear()
        new_password_input.send_keys(user["password"])

        add_button.click()

        time.sleep(2)

        add_message = driver.find_element(By.ID, "addUserMessage")
        assert add_message.text == "Пользователь добавлен!", f"Ошибка при добавлении пользователя {user['login']}"

        # Проверяем авторизацию добавленного пользователя
        login_input = driver.find_element(By.ID, "login")
        password_input = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, "form#loginForm button[type='submit']")

        login_input.clear()
        login_input.send_keys(user["login"])
        password_input.clear()
        password_input.send_keys(user["password"])

        submit_button.click()

        time.sleep(2)

        # Вывод информации для отладки
        message = driver.find_element(By.ID, "loginMessage")
        print(f"Проверка пользователя: {user['login']}")
        print(f"Ожидаемое сообщение: 'Вход успешен!'")
        print(f"Фактическое сообщение: '{message.text}'")

        assert message.text == "Вход успешен!", f"Ошибка при входе для пользователя {user['login']} с паролем {user['password']}: {message.text}"



















