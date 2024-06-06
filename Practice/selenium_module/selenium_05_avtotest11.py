import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера браузера
driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/QA_autotests_11/')
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR,'#imageInput').send_keys(r'C:\Users\AttekPC\Pictures\Без названия.jfif')

    driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()