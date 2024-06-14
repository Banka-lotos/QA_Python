P
# Инициализируем драйвер браузера (в данном случае Chrome)
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get('https://erikdark.github.io/Qa_autotest_02/')
    time.sleep(2)  # Ждем некоторое время, чтобы страница полностью загрузилась

    # Находим все поля ввода
    input_fields = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')

    # Заполняем каждое поле ввода
    for input_field in input_fields:
        input_field.send_keys('Test')  # Здесь можно вставить нужные вам данные

    # Нажимаем кнопку submit
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_button.click()

    # Для наглядности ждем некоторое время, можно убрать это в реальном тестировании
    time.sleep(2)

finally:
    # Закрываем браузер после выполнения скрипта
    driver.quit()

   


