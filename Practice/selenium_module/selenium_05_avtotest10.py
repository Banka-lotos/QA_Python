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
    driver.get('https://erikdark.github.io/QA_autotests_10/')
    time.sleep(1)


    driver.execute_script("document.getElementById('hiddenButton').style.display='block';")
    driver.find_element(By.CSS_SELECTOR,'#hiddenButton').click()
   


finally:
    time.sleep(5)
    driver.quit()
