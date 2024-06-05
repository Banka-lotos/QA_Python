
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By




#иницилизирую драйвер браузера
driver = webdriver.Chrome()




try:
    driver.get('https://erikdark.github.io/Qa_autotest_02/')
    input = driver.find_elements(By.CSS_SELECTOR,'input')
    for i in input:
        i.send_keys('Text')
   
    time.sleep(3)
   


finally:
    driver.quit()


