import time 
#импортирую сам вебдрайвер 
from selenium import webdriver 
#импортирую класс By который ищет элемент на странице 
from selenium.webdriver.common.by import By 
 
 
 
 
#иницилизирую драйвер браузера 
driver = webdriver.Chrome() 
 
try: 
    # Открываем сайт 
    driver.get('https://erikdark.github.io/Qa_autotest_02/') 
     
    # Заполняем поля формы 
    phone_input = driver.find_element(By.ID, 'phone') 
    email_input = driver.find_element(By.ID, 'email') 
    name_input = driver.find_element(By.ID, 'name') 
    password_input = driver.find_element(By.ID, 'password') 
     
    phone_input.send_keys('1234567890') 
    email_input.send_keys('test@example.com') 
    name_input.send_keys('Test User') 
    password_input.send_keys('password123') 
 
    # Кнопка сабмита по умолчанию отключена. Активируем её. 
    driver.execute_script("document.getElementById('submitBtn').removeAttribute('disabled');") 
 
    # Нажимаем на кнопку Submit 
    submit_button = driver.find_element(By.ID, 'submitBtn') 
    submit_button.click() 
     
    # Ожидание появления модального окна 
    time.sleep(2) 
     
    # Проверка, что модальное окно открылось 
    congrats_message = driver.find_element(By.TAG_NAME, 'h1') 
    assert congrats_message.text == 'Поздравляю, вы прошли первый уровень', f"Unexpected message: {congrats_message.text}" 
 
    print("Registration test passed.") 
     
except Exception as e: 
    print(f"An error occurred: {e}") 
 
 
finally: 
    driver.quit()