from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage) :
    signUp_button = (By.ID, "signin2")
    login_button = (By.ID, "login2")

    def open_signup_modal(self):
        self.click(self.signUp_button)
       
    def open_login_modal(self):
        self.click(self.login_button)

    def select_product(self):
        self.click((By.XPATH, "//a[@class='hrefch']"))