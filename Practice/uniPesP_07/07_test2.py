# Импорт необходимых модулей 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
 
# Функция для настройки драйвера 
def setup_driver(): 
    driver = webdriver.Chrome() 
    driver.implicitly_wait(10) 
    return driver 
 
# Функция для заполнения формы регистрации 
def fill_registration_form(driver, username, email, password, confirm_password): 
    # Переход на страницу с формой регистрации 
    driver.get("https://erikdark.github.io/PyTest_01_reg_form/") 
    # Заполнение полей формы 
    driver.find_element(By.ID, "username").send_keys(username) 
    driver.find_element(By.ID, "email").send_keys(email) 
    driver.find_element(By.ID, "password").send_keys(password) 
    driver.find_element(By.ID, "confirm_password").send_keys(confirm_password) 
    # Нажатие кнопки регистрации 
    driver.find_element(By.ID, "register").click() 
 
# Тест успешной регистрации 
def test_successful_registration(): 
    driver = setup_driver() 
    try: 
        # Заполнение формы с правильными данными 
        fill_registration_form(driver, "testuser", "testuser@example.com", "Password123!", "Password123!") 
         
        # Проверка успешной регистрации 
        success_message = driver.find_element(By.ID, "success_message") 
        assert success_message.is_displayed() 
        assert success_message.text == "Registration successful" 
        print("Тест успешной регистрации пройден.") 
    finally: 
        driver.quit() 
 
# Тест регистрации с неверным email 
def test_registration_with_invalid_email(): 
    driver = setup_driver() 
    try: 
        # Заполнение формы с неправильным email 
        fill_registration_form(driver, "testuser", "invalidemail", "Password123!", "Password123!") 
         
        # Проверка сообщения об ошибке email 
        error_message = driver.find_element(By.ID, "email_error") 
        assert error_message.is_displayed() 
        assert error_message.text == "Invalid email address" 
        print("Тест регистрации с неверным email пройден.") 
    finally: 
        driver.quit() 
 
# Запуск тестов 
if name == "__main__": 
    test_successful_registration() 
    test_registration_with_invalid_email()
