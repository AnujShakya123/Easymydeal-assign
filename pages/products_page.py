from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_tab = (By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a")
        self.search_box = (By.XPATH, "/html/body/section[1]/div/input")
        self.search_button = (By.XPATH, "/html/body/section[1]/div/button")
        self.product_names = (By.XPATH, "//div[@class='productinfo text-center']/p")
        self.view_product = (By.XPATH, "//a[text()='View Product']")

    def open_products(self):
        self.driver.find_element(*self.products_tab).click()

    def search_product(self, keyword):
        self.driver.find_element(*self.search_box).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def verify_search_results(self, keyword):
        products = self.driver.find_elements(*self.product_names)
        assert len(products) > 0, "No products found!"
        assert any(keyword.lower() in p.text.lower() for p in products), "Search keyword not found"

    def open_first_product(self):
        self.driver.find_element(*self.view_product).click()
