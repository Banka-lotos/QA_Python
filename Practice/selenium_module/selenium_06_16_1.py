from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
# Инициализация драйвера браузера 
driver = webdriver.Chrome() 
# Ожидание 
driver.implicitly_wait(10) 
 
try: 
    # Откроем веб-страницу 
    driver.get('https://erikdark.github.io/QA_autotest_16/') 
 
    def check_price_and_buy(): 
        while True: 
            for i in range(1, 4): 
                # ищу цену 
                price_element = driver.find_element(By.ID, f'price{i}') 
                price = price_element.text 
                 
                # поверяю =550  
                if price.isdigit() and int(price) == 550: 
                    #нахожу кнопку купить и нажимаю 
                    buy_button = driver.find_element(By.ID, f'buyButton{i}') 
                    buy_button.click() 
 
                    # сообщение что куплена ашина 
                    WebDriverWait(driver, 10).until( 
                        EC.text_to_be_present_in_element((By.ID, f'message{i}'), 'Вы успешно купили автомобиль!') 
                    ) 
                    print(f"Успех: Машина {i} куплена за $550") 
                    return 
 
    check_price_and_buy() 
 
finally: 
    # Закроем веб-драйвер 
    driver.quit()