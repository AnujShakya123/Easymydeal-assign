from selenium.webdriver.common.by import By

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_name = (By.XPATH, "//div[@class='product-information']/h2")
        self.product_price = (By.XPATH, "//div[@class='product-information']//span[contains(text(),'Rs.')]")
        self.add_to_cart_button = (By.XPATH, "//button[@class='btn btn-default cart']")
        self.continue_shopping_button = (By.XPATH, "//button[text()='Continue Shopping']")

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text.strip()

    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text.strip()

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        try:
            self.driver.find_element(*self.continue_shopping_button).click()
        except:
            pass
