
#Решение с WebDriverWait

import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()


try:
    driver.get('https://erikdark.github.io/Qa_autotest_15/')
       
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'verify'))).click()
   
    message = driver.find_element(By.ID,'verify_message')
    assert 'Verification successful!' in message.text
       
       
finally:
    time.sleep(5)
    driver.quit()
