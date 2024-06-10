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
    # input1 = driver.find_element(By.CSS_SELECTOR,'#firstName')
    # input1.send_keys('text')
    # input1 = driver.find_element(By.CSS_SELECTOR,'#lastName')
    # input1.send_keys('text')
    # input1 = driver.find_element(By.CSS_SELECTOR,'#email')
    # input1.send_keys('text@mail.ru')


    #проверяет не обязательные поля.
    # input1 = driver.find_element(By.CSS_SELECTOR,'#phone')
    # input1.send_keys('1231231231')
    # input1 = driver.find_element(By.CSS_SELECTOR,'#address')
    # input1.send_keys('text@mail.ru')
   
   
    btn = driver.find_element(By.CSS_SELECTOR, 'button')
    btn.click()
    time.sleep(1)
    wel_text = driver.find_element(By.CSS_SELECTOR,'h2')
    wel_text_block = wel_text.text


    assert 'Поздравляю, вы прошли первый уровень.' == wel_text_block
   
   


finally:
    time.sleep(5)
    driver.quit()



