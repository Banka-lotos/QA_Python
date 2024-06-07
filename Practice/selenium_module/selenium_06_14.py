#SPA приложения.

#SIngle-page-Application - это страничка сайта на которой контент динамически изменяется посредством JavaScript и REST API. Соответственно , меняется текст, картинки, кнопки и так далее. Что затрудняет выполнения автотестов.

#https://erikdark.github.io/QA_autotests_14/

#код к этой задаче
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
    driver.get('https://erikdark.github.io/QA_autotests_14/')
   
    btn = driver.find_element(By.ID,'verify').click()
    message = driver.find_element(By.ID,'verify_message')
    assert 'Verification successful!' in message.text
   
   
finally:
    time.sleep(5)
    driver.quit()




#А вот код с задержкой 
#import time
#импортирую сам вебдрайвер
#from selenium import webdriver
#импортирую класс By который ищет элемент на странице
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#import re


#иницилизирую драйвер браузера
#driver = webdriver.Chrome()

#try:
 #   driver.get('https://erikdark.github.io/QA_autotests_14/')
  #  time.sleep(1)
   # btn = driver.find_element(By.ID,'verify').click()
    #message = driver.find_element(By.ID,'verify_message')
    #assert 'Verification successful!' in message.text
   
   
#finally:
 #   time.sleep(5)
  #  driver.quit()



