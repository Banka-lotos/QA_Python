
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
import re


#иницилизирую драйвер браузера
driver = webdriver.Chrome()


try:
    driver.get('https://erikdark.github.io/Qa_autotest_07/')
    time.sleep(2)
   
    nums = driver.find_element(By.CSS_SELECTOR,'#numberImage')
    b = nums.get_attribute('data-b')
    b = b.split('?')
   


    anser = int(b[0] + b[1])
   


    text = driver.find_element(By.CSS_SELECTOR,'#answer').send_keys(anser)
    driver.find_element(By.CSS_SELECTOR,'#submitBtn').click()




finally:
    time.sleep(5)
    driver.quit()