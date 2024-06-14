import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_data_table(driver):
    driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
    
    # Находим и нажимаем кнопку "Таблица данных"
    table_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Таблица данных"))
    )
    table_link.click()

def get_column_data(driver, column_index):
    rows = driver.find_elements(By.CSS_SELECTOR, "#data-table tbody tr")
    return [row.find_elements(By.TAG_NAME, "td")[column_index].text for row in rows]

def check_sorting(driver, column_index):
    original_data = get_column_data(driver, column_index)

    # Нажимаем на заголовок колонки для сортировки
    header = driver.find_elements(By.CSS_SELECTOR, "#data-table th")[column_index]
    header.click()
    
    # Ожидаем обновления данных после сортировки
    WebDriverWait(driver, 10).until(
        EC.staleness_of(header)
    )
    
    # Получаем отсортированные данные
    sorted_data = get_column_data(driver, column_index)

    # Проверка сортировки
    assert sorted_data == sorted(original_data), f"Данные в колонке {column_index} не отсортированы"
    
    # Проверка сообщения
    message = driver.find_element(By.ID, "sort-message").text
    expected_message = f"Таблица отсортирована по столбцу {column_index + 1}"
    assert message == expected_message, f"Ожидалось сообщение '{expected_message}', но '{message}'"
    print(message)

@pytest.mark.usefixtures("open_data_table")
def test_sorting(driver):
    for column_index in range(3):
        check_sorting(driver, column_index)