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
    driver.get('https://erikdark.github.io/QA_autotests_09/')
    time.sleep(1)
    a_clenge = driver.find_element(By.CSS_SELECTOR,'#challenge').text.split()
    a = int(a_clenge[2])
    b = int(a_clenge[4].replace('?',''))
    answer = a+b


    select = Select(driver.find_element(By.TAG_NAME,'select'))
    select.select_by_value(str(answer))


    driver.find_element(By.CSS_SELECTOR,'#submitBtn').click()


    message = driver.find_element(By.CSS_SELECTOR,'#message').text


    assert 'You guessed it! Well done!' == message
    
   

finally:
    time.sleep(5)
    driver.quit()



    