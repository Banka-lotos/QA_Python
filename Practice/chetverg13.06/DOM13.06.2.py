from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


link = "https://koshelek.ru/authorization/signup"


class TestRegForm_negative(unittest.TestCase):
    def test_negative_1(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            time.sleep(5)


            container = browser.find_element(By.CSS_SELECTOR, ".remoteComponent")
            container_shadow = container.shadow_root
            inputs = container_shadow.find_elements(By.CSS_SELECTOR, "input")


            # первое обязательное поле - имя:
            input_field = inputs[0]
            input_field.send_keys("Алиса")
            time.sleep(3)
           
            # Очистка поля ввода
            browser.execute_script("arguments[0].value = 'Alisa'", input_field)


            # Для демонстрации
            time.sleep(2)
           
        finally:
            time.sleep(5)
            browser.quit()


if __name__ == "__main__":
    unittest.main()
