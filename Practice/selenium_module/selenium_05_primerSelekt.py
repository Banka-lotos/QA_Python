
#более подробно

import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()


try:
    driver.get('https://erikdark.github.io/QA_autotests_08/')
    time.sleep(2)
    #подробно каждый шаг
    first_select_container = driver.find_element(By.CSS_SELECTOR,'.container')
    first_select_container.find_element(By.CSS_SELECTOR,'select').click()
    first_select_container.find_element(By.CSS_SELECTOR,'option:nth-child(2)').click()
    #или каждый шаг прописан в 1 запрос
    driver.find_element(By.CSS_SELECTOR,'.container-main select option:nth-child(2)').click()
   

finally:
    time.sleep(5)
    driver.quit()





