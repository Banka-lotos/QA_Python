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
 
# проверка сущ польз
def test_existing_users_validation(open_login_form): 
    driver = open_login_form 
 
    users = [ 
        {"login": "user1", "password": "Pass1234"}, 
        {"login": "user2", "password": "Pass1234"}, 
        {"login": "user3", "password": "Pass1234"}, 
        {"login": "user4", "password": "Pass1234"}, 
        {"login": "user5", "password": "Pass1234"} 
    ] 
 
    for user in users: 
        login_input = driver.find_element(By.ID, "login") 
        password_input = driver.find_element(By.ID, "password") 
        submit_button = driver.find_element(By.CSS_SELECTOR, "form#loginForm button[type='submit']") 
 
        login_input.clear() 
        login_input.send_keys(user["login"]) 
        password_input.clear() 
        password_input.send_keys(user["password"]) 
 
        submit_button.click() 
 
        time.sleep(2) 
 
        message = driver.find_element(By.ID, "loginMessage") 
         
        # Проверяем успешный вход 
        if message.text == "Неверный логин или пароль": 
            assert message.text == "Неверный логин или пароль", f"Ожидалось 'Неверный логин или пароль', получено '{message.text}'" 
        else: 
            assert message.text == "Вход успешен!", f"Ожидалось 'Вход успешен!', получено '{message.text}'" 
 
# новый польз 
def test_new_user_validation(open_login_form): 
    driver = open_login_form 
 
    new_login = "newuser" 
    new_password = "NewPaswr1234" 
 
    new_login_input = driver.find_element(By.ID, "newLogin") 
    new_password_input = driver.find_element(By.ID, "newPassword") 
    add_button = driver.find_element(By.CSS_SELECTOR, "form#addUserForm button[type='submit']") 
 
    new_login_input.clear() 
    new_login_input.send_keys(new_login) 
    new_password_input.clear() 
    new_password_input.send_keys(new_password) 
 
    add_button.click() 
 
    time.sleep(2) 
 
    add_message = driver.find_element(By.ID, "addUserMessage") 
    assert add_message.text == "Пользователь добавлен!" 
 
# Тест для проверки валидации нескольких новых пользователей 
def test_multiple_users_validation(open_login_form): 
    driver = open_login_form 
 
    new_users = [ 
        {"login": "MENYA", "password": "Qwer12*4"},
        {"login": "YZHE", "password": "Qwer12*SD"},
        {"login": "BESIT", "password": "Pa87r12KL"},
      
    ] 
 
    for user in new_users: 
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
        assert add_message.text == "Пользователь добавлен!"