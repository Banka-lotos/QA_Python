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
    driver.get('https://erikdark.github.io/QA_autotests_13/')
    time.sleep(1)


    driver.find_element(By.CSS_SELECTOR,'#openNewPageBtn').click()
    time.sleep(1)


    new_tab = driver.window_handles[1]
    driver.switch_to.window(new_tab)


    driver.find_element(By.CSS_SELECTOR,'#displayTextBtn').click()


    display_text = driver.find_element(By.CSS_SELECTOR,'#displayText').text


    assert display_text == 'Я СДЕЛАЛ', 'текст не отображается или не верный текст'
    print('Test compleate!')
   
   




finally:
    time.sleep(5)
    driver.quit()


