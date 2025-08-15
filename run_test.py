from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Import POM classes
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    product_detail = ProductDetailPage(driver)
    cart_page = CartPage(driver)

    # Step 1: Login
    login_page.open()
    time.sleep(2)
    login_page.login("anujshakya808@gmail.com", "Anuj@8645")
    time.sleep(2)
    login_page.verify_login()

    # Step 2: Search product
    products_page.open_products()
    time.sleep(2)
    products_page.search_product("Jeans")
    time.sleep(2)
    products_page.verify_search_results("Jeans")

    # Step 3: Open first product
    products_page.open_first_product()
    time.sleep(2)
    name = product_detail.get_product_name()
    price = product_detail.get_product_price()

    # Step 4: Add to cart
    product_detail.add_to_cart()
    time.sleep(2)

    # Step 5: Go to cart and verify
    cart_page.open()
    time.sleep(2)
    cart_page.verify_cart_item(name, price)

    print(" Test passed: Search & Cart verification successful")

finally:
    driver.quit()
