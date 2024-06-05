import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера браузера
driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotests_05/')
    time.sleep(2)

    # Найти и прочитать значения для подсчета суммы
    challenge_text = driver.find_element(By.ID, 'challenge').text
    print("Challenge text:", challenge_text)

    
    # Извлекаем числа из строки, например, "Сколько будет 3+97?"
    numbers = list(map(int, re.findall(r'\d+', challenge_text)))
    sum_result = sum(numbers)
    print("Sum result:", sum_result)

    # Ввести результат в поле ответа
    answer_input = driver.find_element(By.ID, 'answer')
    answer_input.clear()
    answer_input.send_keys(str(sum_result))

    # Выбрать нужные опции
    not_robot_checkbox = driver.find_element(By.ID, 'notRobot')
    human_checkbox = driver.find_element(By.ID, 'human')
    cool_radio = driver.find_element(By.ID, 'cool')

    if not_robot_checkbox.is_selected() is False:
        not_robot_checkbox.click()
    if human_checkbox.is_selected() is False:
        human_checkbox.click()
    if cool_radio.is_selected() is False:
        cool_radio.click()

    # Нажать на кнопку
    submit_btn = driver.find_element(By.ID, 'submitBtn')
    submit_btn.click()
    time.sleep(2)

    # Проверить текст
    result_text = driver.find_element(By.CSS_SELECTOR, 'h2').text
    print("Result text:", result_text)
    assert 'Congratulations, Elon Musk!' in result_text

finally:
    time.sleep(5)
    driver.quit()