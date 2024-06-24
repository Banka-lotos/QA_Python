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
def open_magaz_form(setup_driver):
    driver = setup_driver
    driver.get("https://erikdark.github.io/QA_DIPLOM/")

    magaz_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Магазин"))
    )
    magaz_link.click()

    return driver

def test_add_to_cart(open_magaz_form):
    driver = open_magaz_form

    # Проверяемые продукты
    products = [
        {"name": "Товар 1", "price": 100},
        {"name": "Товар 2", "price": 200},
        {"name": "Товар 3", "price": 300}
    ]

    # Добавление товаров в корзину
    for product in products:
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[@data-name='{product['name']}']"))
        )
        add_button.click()

        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            assert f"{product['name']} добавлен в корзину" in alert.text
            alert.accept()
        except Exception as e:
            print(f"No alert present after adding {product['name']}: {e}")

        time.sleep(2)  # Даем странице время для обновления

    # Переходим в корзину
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cartButton"))
    )
    cart_button.click()

    time.sleep(2)  # Даем странице время для загрузки элементов корзины

    # Проверяем, что все товары добавлены в корзину
    cart_items = driver.find_elements(By.XPATH, "//div[@id='cartItems']/div")
    assert len(cart_items) == len(products), f"Ожидали {len(products)} товара(ов) в корзине, получили {len(cart_items)}"

    # Проверяем количество добавлений каждого товара в корзину
    for product in products:
        item_text = f"{product['name']} - ${product['price']}"
        count = sum(1 for item in cart_items if item.text == item_text)
        assert count == 1, f"Товар {product['name']} добавлен {count} раз(а) вместо одного"

    # Переходим обратно в магазин для проверки цен на товары
    driver.get("https://erikdark.github.io/QA_DIPLOM/")  

    # Проверяем стоимость товаров в магазине
    for product in products:
        product_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='product']//h3[text()='{product['name']}']/following-sibling::p"))
        )
        assert f"Цена: ${product['price']}" in product_element.text

    # Переходим в корзину для сравнения стоимости
    cart_button.click()
    time.sleep(2)  # Даем странице время для загрузки элементов корзины

    # Проверяем стоимость товаров в корзине
    for product in products:
        cart_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@id='cartItems']/div[contains(text(), '{product['name']}')]"))
        )
        cart_item_price = cart_item.text.split(' - ')[-1]  # Получаем цену товара в корзине
        assert f"${product['price']}" in cart_item_price, f"Цена товара {product['name']} в корзине отличается от {product['price']}"

    # Проверяем общую стоимость в корзине
    total_in_cart = driver.find_element(By.ID, "cartTotal").text
    expected_total = sum(product['price'] for product in products)
    assert f"Общая стоимость: ${expected_total}" in total_in_cart