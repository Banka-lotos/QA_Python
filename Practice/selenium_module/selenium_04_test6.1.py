import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()


try:
    driver.get('https://erikdark.github.io/Qa_autotests_05/')
    time.sleep(2)
    text_challange = driver.find_element(By.CSS_SELECTOR,'#challenge').text


    #без регулярных выражений
    # words = text_challange.split()
    # a = int(words[2])
    # b = int(words[4].replace('?',''))
    # print(words)
    # anser = a+ b


    #с регулярными выражениями


    nums = re.findall(r'\d+',text_challange)
    print(nums)
    a = int(nums[0])
    b = int(nums[1])
    anser = a+b


    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(anser))


    driver.find_element(By.CSS_SELECTOR, '#notRobot').click()


    driver.find_element(By.CSS_SELECTOR, '#cool').click()


    driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()




    text = driver.find_element(By.CSS_SELECTOR,'#message').text


    assert 'Поздравляю, Elon Musk!' == text




finally:
    time.sleep(5)
    driver.quit()


