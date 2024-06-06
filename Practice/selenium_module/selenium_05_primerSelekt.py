#Пример с Select

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
    select = Select(driver.find_element(By.TAG_NAME,'select'))
    select.select_by_value('5')
   
   




finally:
    time.sleep(5)
    driver.quit()


