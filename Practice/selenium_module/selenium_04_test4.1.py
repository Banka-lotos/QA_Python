#ЧЕРЕЗ requiered 
 
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By




#иницилизирую драйвер браузера
driver = webdriver.Chrome()




try:
    driver.get('https://erikdark.github.io/Qa_autotest_03/')
    #проверили обязательные поля
    input1 = driver.find_elements(By.CSS_SELECTOR,'[required]')
    for i in input1:
        i.send_keys('test')


   
   
   
    btn = driver.find_element(By.CSS_SELECTOR, 'button')
    btn.click()
    time.sleep(1)
    wel_text = driver.find_element(By.CSS_SELECTOR,'h2')
    wel_text_block = wel_text.text


    assert 'Поздравляю, вы прошли первый уровень.' == wel_text_block
   
   


finally:
    time.sleep(5)
    driver.quit()


