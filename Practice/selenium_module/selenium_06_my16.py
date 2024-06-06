from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализирую драйвер браузера
driver = webdriver.Chrome()

# Устанавливаю implicit wait
driver.implicitly_wait(10)

try:
    # Открываю веб-страницу
    driver.get('https://erikdark.github.io/QA_autotest_16/')

    # Локаторы для элементов
    price_locator_template = 'price{}'
    buy_button_locator_template = 'buyButton{}'
    message_locator_template = 'message{}'

    def check_price_and_buy():
        for i in range(1, 4):
            try:
                # Получаю элемент цены и проверяю текущее значение
                price_element = driver.find_element(By.ID, price_locator_template.format(i))
                current_price = int(price_element.text.strip())

                # Проверяю, если цена равна 550
                if current_price == 550:
                    # Нажимаю кнопку "Купить"
                    buy_button = driver.find_element(By.ID, buy_button_locator_template.format(i))
                    buy_button.click()

                    # Ожидаю появления сообщения об успешной покупке
                    WebDriverWait(driver, 10).until(
                        EC.text_to_be_present_in_element((By.ID, message_locator_template.format(i)), 'Вы успешно купили автомобиль!')
                    )
                    print(f"Успех: Машина {i} куплена за $550")
                    return True
            except Exception as e:
                print(f"Ошибка при проверке машины {i}: {e}")
        return False

    while not check_price_and_buy():
        pass

finally:
    driver.quit()