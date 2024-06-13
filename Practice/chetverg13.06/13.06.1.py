
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get('https://erikdark.github.io/dovod_repo_QA_form/')


#найти элементы
l_i = driver.find_element(By.ID,'login')
p_i = driver.find_element(By.ID,'password')
d_i = driver.find_element(By.ID,'database')
h_i = driver.find_element(By.ID,'host')
s_b = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')


#заполнил форму
l_i.send_keys('admin123')
p_i.send_keys('password123')
d_i.send_keys('bd_dovod')
h_i.send_keys('localhost')

#отправляю форму
s_b.click()


alert = driver.switch_to.alert
alert.accept()

#очищаю поля

l_i.clear()
p_i.clear()
d_i.clear()
h_i.clear()


h_i.send_keys('tsohlacol')
d_i.send_keys('dovod_db')
p_i.send_keys('321drowssap')
l_i.send_keys('321nimda')

s_b.click()

