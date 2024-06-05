import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_and_submit(driver, inputs_data):
    for selector, text in inputs_data.items():
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        input_field.clear()  # Очищаем поле перед вводом
        input_field.send_keys(text)
    
    # Ждем появления кнопки и кликаем на нее
    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button'))
    )
    btn.click()
    
    # Ждем появления h2 элемента с текстом
    wel_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h2'))
    )
    
    wel_text_block = wel_text.text
    return wel_text_block

# Инициализирую драйвер браузера
driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotest_03/')
    
    # Тест 1: Все обязательные поля
    mandatory_fields = {
        'input[required]': 'Text@mail.ru'
    }
    result = fill_and_submit(driver, mandatory_fields)
    assert 'Поздравляю, вы прошли первый уровень.' == result

    # Возвращаемся на начальную страницу для следующего теста
    driver.get('https://erikdark.github.io/Qa_autotest_03/')

    # Тест 2: Все необязательные поля
    optional_fields = {
        'input:not([required])': 'OptionalText'
    }
    result = fill_and_submit(driver, optional_fields)
    assert 'Поздравляю, вы прошли первый уровень.' == result

finally:
    time.sleep(5)  # для демонстрации, можно убрать или уменьшить
    driver.quit()