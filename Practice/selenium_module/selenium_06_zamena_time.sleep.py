
#Замена Time.sleep()
#Implicit_wait Который заложен в Selenium Waits

import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()
driver.implicitly_wait(5)


try:
    driver.get('https://erikdark.github.io/QA_autotests_14/')
       
    btn = driver.find_element(By.ID,'verify').click()
    message = driver.find_element(By.ID,'verify_message')
    assert 'Verification successful!' in message.text
       
       
finally:
    time.sleep(5)
    driver.quit()