
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера браузера
driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotest_04/')
    time.sleep(2)

    # Проверка обязательных полей (имя и фамилия могут быть с 1 буквой или любым символом)
    name_input = driver.find_element(By.ID, "name")
    name_input.clear()
    name_input.send_keys("A")

    last_name_input = driver.find_element(By.ID, "lastName")
    last_name_input.clear()
    last_name_input.send_keys("@")

    # Проверка корректности email
    email_input = driver.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys("example.email.com")  # некорректный email

    time.sleep(1)  # Задержка для появления сообщения об ошибке

    try:
        error_message_email = driver.find_element(By.XPATH, "//span[contains(text(), 'Укажите корректный email')]")
        print("Некорректный email: " + error_message_email.text)  # вывод сообщения об ошибке, если он появляется
    except:
        print("Сообщение об ошибке email не найдено.")

    email_input.clear()
    email_input.send_keys("example@example.com")  # корректный email

    time.sleep(2)

    # Проверка ввода номера телефона (+7 должно добавиться автоматически)
    phone_number_input = driver.find_element(By.ID, "phoneNumber")
    phone_number_input.clear()
    phone_number_input.send_keys("1234567890")

    time.sleep(2)

    phone_value = phone_number_input.get_attribute('value')
    print("Значение поля номера телефона: " + phone_value)  # вывод значения поля номера телефона для проверки

    # Проверка необязательных полей
    address_input = driver.find_element(By.ID, "address")
    address_input.clear()
    address_input.send_keys("Some address")

    # Нажатие кнопки для завершения формы
    btn = driver.find_element(By.CSS_SELECTOR, 'button')
    btn.click()
    time.sleep(1)

    # Проверка сообщения о завершении
    wel_text = driver.find_element(By.CSS_SELECTOR, 'h2')
    wel_text_block = wel_text.text
    assert 'Поздравляю, вы прошли первый уровень.' == wel_text_block

finally:
    time.sleep(5)
    driver.quit()