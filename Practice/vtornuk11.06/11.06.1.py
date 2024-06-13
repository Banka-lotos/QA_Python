import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_buy_books(driver):
    # Открыть сайт
    driver.get("http://selenium1py.pythonanywhere.com/ru/")
    
    # Нажать на кнопку "Предложения"
    offers_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Предложения")))
    offers_link.click()
    
    # Добавить книги в корзину
    for i in range(1, 5):
        book_xpath = f"//button[@data-loading-text='Добавление...'][{i}]"
        add_to_basket_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, book_xpath)))
        add_to_basket_button.click()
    
    # Перейти в корзину
    basket_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Посмотреть корзину")))
    basket_link.click()
    
    # Нажать на кнопку "Перейти к оформлению"
    proceed_to_checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Перейти к оформлению")))
    proceed_to_checkout_button.click()
    
    # Ввести email
    email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_username")))
    email_input.send_keys("ваша_почта@gmail.com")
    
    # Выбрать опцию "новый пользователь"
    new_user_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_options_1")))
    new_user_option.click()
    
    # Ввести пароль
    password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_password")))
    password_input.send_keys("ваш_пароль")
    
    # Нажать кнопку "Продолжить"
    continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-loading-text='Продолжаем...']")))
    continue_button.click()
    
    # Ввести пароль еще раз для подтверждения
    confirm_password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_password1")))
    confirm_password_input.send_keys("ваш_пароль")
    
    # Подтвердить пароль
    confirm_password_input2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_password2")))
    confirm_password_input2.send_keys("ваш_пароль")
    
    # Нажать кнопку "Зарегистрироваться"
    register_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='registration_submit'][data-loading-text='Регистрация...']")))
    register_button.click()
    
    # Заполнить личные данные
    first_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_first_name")))
    first_name_input.send_keys("Ваше_имя")
    
    last_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_last_name")))
    last_name_input.send_keys("Ваша_фамилия")
    
    address_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_line1")))
    address_input.send_keys("Ваш_адрес")
    
    city_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_line4")))
    city_input.send_keys("Ваш_город")
    
    postal_code_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_postcode")))
    postal_code_input.send_keys("Ваш_почтовый_индекс")
    
    phone_number_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_phone_number")))
    phone_number_input.send_keys("Ваш_номер_телефона")
    
    # Нажать кнопку "Продолжить"
    continue_button_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-loading-text='Продолжаем...']")))
    continue_button_2.click()

if __name__ == "__main__":
    pytest.main()