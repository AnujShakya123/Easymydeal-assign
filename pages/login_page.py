from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_link = (By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")
        self.login_email = (By.XPATH, "//input[@data-qa='login-email']")
        self.login_password = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_button = (By.XPATH, "//button[@data-qa='login-button']")
        self.logged_in_text = "Logged in as"

    def open(self):
        self.driver.get("https://automationexercise.com/")
        self.driver.find_element(*self.login_link).click()

    def login(self, email, password):
        self.driver.find_element(*self.login_email).send_keys(email)
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def verify_login(self):
        assert self.logged_in_text in self.driver.page_source, "Login failed!"
