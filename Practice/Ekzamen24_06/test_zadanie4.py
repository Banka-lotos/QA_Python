import pytest 
import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
@pytest.fixture 
def setup_driver(): 
    driver = webdriver.Chrome() 
    yield driver 
    driver.quit() 
 
@pytest.fixture 
def open_bd_form(setup_driver): 
    driver = setup_driver 
    driver.get("https://erikdark.github.io/QA_DIPLOM/") 
 
    bd_link = WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.LINK_TEXT, "База данных")) 
    ) 
    bd_link.click() 
 
    return driver 
 
def test_sql_operations(open_bd_form): 
    driver = open_bd_form 
 
    # Запросы 
    queries = [ 
        "SELECT * FROM TABLE WHERE NAME = 'Иван'", 
        "ORDER BY AGE", 
        "DELETE FROM TABLE WHERE ID = 1" 
    ] 
 
    for query in queries: 
        # Поле ввода запроса 
        sql_query_input = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.ID, "sqlQuery")) 
        ) 
        sql_query_input.clear() 
        sql_query_input.send_keys(query) 
 
        # Кнопка "Выполнить" 
        execute_button = driver.find_element(By.ID, "executeButton") 
        execute_button.click() 
 
        # Визуальное ожидание для обновления страницы 
        time.sleep(4)  # Пауза в 2 секунды (можно адаптировать по необходимости) 
 
        # Сообщение о выполнении SQL запроса 
        sql_message = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.ID, "sqlMessage")) 
        ).text 
 
        # Проверка выполнения запроса 
        if query.startswith("SELECT"): 
            assert "Найдено" in sql_message and "записей." in sql_message, f"Ожидалось 'Найдено записей.', получено '{sql_message}'" 
        elif query.startswith("ORDER BY"): 
            assert "Данные отсортированы" in sql_message, f"Ожидалось 'Данные отсортированы.', получено '{sql_message}'" 
        elif query.startswith("DELETE"): 
            assert "удалена." in sql_message, f"Ожидалось 'удалена.', получено '{sql_message}'"