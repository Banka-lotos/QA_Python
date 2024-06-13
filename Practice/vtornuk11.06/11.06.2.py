import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope='function')
def driver():
    # Инициализация драйвера браузера
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()

def test_order_books(driver):
    # Открыть сайт
    driver.get("http://selenium1py.pythonanywhere.com/ru/")
    
    # Перейти в раздел "Предложения"
    offers_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Предложения"))
    )
    offers_link.click()
    
    # Задержка для надежной загрузки страницы
    time.sleep(3)

    # Индексы кнопок для добавления книг в корзину
    indexes_to_click = [0, 1, 2, 3]

    # Добавить книги в корзину
    for i in indexes_to_click:
        try:
            add_to_basket_buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
            add_to_basket_buttons[i].click()
            print(f'Книга {i} добавлена в корзину')
            time.sleep(2)  # Задержка для обработки добавления в корзину
        except:
            print(f'Не удалось добавить книгу {i}')
    
    # Перейти в корзину
    basket_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Посмотреть корзину"))
    )
    basket_link.click()
    
    # Перейти к оформлению заказа
    checkout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Перейти к оформлению"))
    )
    checkout_link.click()
    
    # Заполнить данные оформления заказа
    email_input = driver.find_element(By.ID, "id_username")
    email_input.send_keys("sssnakeee@gmail.com")
    
    new_user_radio = driver.find_element(By.ID, "id_options_1")
    new_user_radio.click()
    
    password_input = driver.find_element(By.ID, "id_password")
    password_input.send_keys("FfFjkl123!")
    
    continue_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Продолжить']")
    continue_button.click()
    
    # Задержка для надежной загрузки страницы
    time.sleep(3)
    
    password_confirm_input = driver.find_element(By.ID, "id_password1")
    password_confirm_input.send_keys("FfFjkl123!")
    
    password_confirm_confirm_input = driver.find_element(By.ID, "id_password2")
    password_confirm_confirm_input.send_keys("FfFjkl123!")
    
    register_button = driver.find_element(By.XPATH, "//button[@name='registration_submit' and @value='Register']")
    register_button.click()
    
    first_name_input = driver.find_element(By.ID, "id_first_name")
    first_name_input.send_keys("AAAAAA")
    
    last_name_input = driver.find_element(By.ID, "id_last_name")
    last_name_input.send_keys("AAAAAABB")
    
    address_input = driver.find_element(By.ID, "id_line1")
    address_input.send_keys("Спасская дом 1 корпус 1")
    
    city_input = driver.find_element(By.ID, "id_line4")
    city_input.send_keys("Питер")
    
    postcode_input = driver.find_element(By.ID, "id_postcode")
    postcode_input.send_keys("198266")
    
    phone_number_input = driver.find_element(By.ID, "id_phone_number")
    phone_number_input.send_keys("+79219898991")
    
    continue_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Продолжить']")
    continue_button.click()
    
    view_preview_button = driver.find_element(By.ID, "view_preview")
    view_preview_button.click()
    
    proceed_button = driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']")
    proceed_button.click()
    
    place_order_button = driver.find_element(By.ID, "place-order")
    place_order_button.click()
    
    # Проверить, что заказ успешно размещен
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-success') and contains(@class, 'alert-safe') and contains(@class, 'alert-noicon') and contains(@class, 'fade') and contains(@class, 'in')]"))
    )
    assert "Спасибо! Ваш заказ был успешно обработан" in success_message.text