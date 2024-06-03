import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем драйвер браузера
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get('https://erikdark.github.io/Qa_autotest_01/')
    time.sleep(2)

    # Находим все кнопки на странице
    buttons_on_page = driver.find_elements(By.TAG_NAME, 'button')

    # Заданное количество кнопок
    expected_buttons_count = 56

    # Сравниваем фактическое количество с заданным
    if len(buttons_on_page) == expected_buttons_count:
        print("Фактическое совпадает.")
    else:
        print("Факт НЕ совпадает.")

finally:
    # Закрываем браузер
    driver.quit()