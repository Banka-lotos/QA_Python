import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
import re




#иницилизирую драйвер браузера
driver = webdriver.Chrome()




try:
    driver.get('https://erikdark.github.io/QA_autotests_08/')
    time.sleep(2)
    driver.find_element(By.TAG_NAME,'select').click()
    driver.find_element(By.CSS_SELECTOR,'option:nth-child(2)').click()
   


finally:
    time.sleep(5)
    driver.quit()