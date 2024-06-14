
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://selenium1py.pythonanywhere.com/ru/offers/')


indexs_to_click = [0,2,4,6,14,16]


for i in indexs_to_click:
    try:
        btn = driver.find_elements(By.CSS_SELECTOR,'button.btn.btn-primary.btn-block')
        btn[i].click()
        print(f'[{i}] нннн куплен')
    except:
        print(f'[{i}] хрень какая-то')


#ДОДЕЛАТЬ КОД
