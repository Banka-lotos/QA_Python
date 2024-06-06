
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By




#иницилизирую драйвер браузера
driver = webdriver.Chrome()




try:
    driver.get('https://easysmarthub.ru/blog/')
    time.sleep(5)
    link = driver.find_element(By.LINK_TEXT, 'Что такое базы данных?')
    link.click()
    time.sleep(2)
    link = driver.find_element(By.LINK_TEXT, 'Эрик Спичак')
    link.click()
    time.sleep(5)


finally:
    driver.quit()
