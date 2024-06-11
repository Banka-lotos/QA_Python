import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    # Добавить книги в корзину
    book_images = driver.find_elements(By.CSS_SELECTOR, "img.thumbnail")
    for book_image in book_images:
        book_image.click()
        add_to_basket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary.btn-block"))
        )
        add_to_basket_button.click()
        driver.back()  # Возвращаемся к списку книг

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
    email_input.send_keys("exemple@gmail.com")
    
    new_user_radio = driver.find_element(By.ID, "id_options_1")
    new_user_radio.click()
    
    password_input = driver.find_element(By.ID, "id_password")
    password_input.send_keys("qwerty12345")
    
    continue_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Продолжить']")
    continue_button.click()
    
    password_confirm_input = driver.find_element(By.ID, "id_password1")
    password_confirm_input.send_keys("qwerty12345")
    
    password_confirm_confirm_input = driver.find_element(By.ID, "id_password2")
    password_confirm_confirm_input.send_keys("qwerty12345")
    
    register_button = driver.find_element(By.XPATH, "//button[@name='registration_submit' and @value='Register']")
    register_button.click()
    
    first_name_input = driver.find_element(By.ID, "id_first_name")
    first_name_input.send_keys("petr")
    
    last_name_input = driver.find_element(By.ID, "id_last_name")
    last_name_input.send_keys("petr")
    
    address_input = driver.find_element(By.ID, "id_line1")
    address_input.send_keys("qwerty 12")
    
    city_input = driver.find_element(By.ID, "id_line4")
    city_input.send_keys("Istanbul")
    
    postcode_input = driver.find_element(By.ID, "id_postcode")
    postcode_input.send_keys("34001")
    
    country_dropdown = driver.find_element(By.ID, "id_country")
    for option in country_dropdown.find_elements(By.TAG_NAME, 'option'):
        if option.text == 'Turkey':
            option.click()
            break
    
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