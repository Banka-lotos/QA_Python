from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit




def test_successful_reg(driver):
    driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
    in1 = driver.find_element(By.CSS_SELECTOR,'#username').send_keys('Erik')
    in1 = driver.find_element(By.CSS_SELECTOR,'#email').send_keys('Erik@mail.ru')
    in1 = driver.find_element(By.CSS_SELECTOR,'#password').send_keys('Erik123')
    btn = driver.find_element(By.CSS_SELECTOR,'button').click()
    message = driver.find_element(By.CSS_SELECTOR,'#success-message').text
    assert message == 'Вы успешно зарегистрированы!', 'Не нашел текст или ты рукожоп...'


def test_successful_reg1(driver):
    driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
    in1 = driver.find_element(By.CSS_SELECTOR,'#username').send_keys('Erik')
    in1 = driver.find_element(By.CSS_SELECTOR,'#email').send_keys('@mail.ru')
    in1 = driver.find_element(By.CSS_SELECTOR,'#password').send_keys('Erik123')
    btn = driver.find_element(By.CSS_SELECTOR,'button').click()
    message = driver.find_element(By.CSS_SELECTOR,'#success-message').text
    assert message == 'Вы успешно зарегистрированы!', 'почта не прошла'
