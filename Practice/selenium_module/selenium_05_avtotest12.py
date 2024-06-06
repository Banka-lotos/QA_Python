
import time 
#импортирую сам вебдрайвер 
from selenium import webdriver 
#импортирую класс By который ищет элемент на странице 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select 
import re 
 
# Инициализация драйвера браузера 
driver = webdriver.Chrome() 
 
try: 
    # Открытие страницы 
    driver.get("https://erikdark.github.io/QA_autotests_12/") 
 
    # Нажатие на кнопку 
    button = driver.find_element(By.ID, "startTaskBtn") 
    button.click() 
    time.sleep(2) 
 
    # Согласие с конфирмом 
    alert = driver.switch_to.alert 
    alert.accept() 
    time.sleep(2) 
 
    # Решение промпт 
    prompt = driver.switch_to.alert 
    prompt.send_keys("50") 
    prompt.accept() 
    time.sleep(3) 
 
    # Проверка текста внутри алерта 
    alert_text = driver.switch_to.alert.text 
    if alert_text == "Правильно! Ответ 50.": 
        print("Текст алерта совпадает с ожидаемым.") 
    else: 
        print("Текст алерта не совпадает с ожидаемым.") 
 
finally: 
    time.sleep(5) 
    driver.quit()