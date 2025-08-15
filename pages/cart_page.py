from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_name = (By.XPATH, "//td[@class='cart_description']/h4/a")
        self.cart_price = (By.XPATH, "//td[@class='cart_price']/p")

    def open(self):
        self.driver.get("https://automationexercise.com/view_cart")

    def verify_cart_item(self, expected_name, expected_price):
        cart_name = self.driver.find_element(*self.cart_name).text.strip()
        cart_price = self.driver.find_element(*self.cart_price).text.strip()
        assert expected_name == cart_name, f"Name mismatch: {expected_name} != {cart_name}"
        assert expected_price == cart_price, f"Price mismatch: {expected_price} != {cart_price}"
