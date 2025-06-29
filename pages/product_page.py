from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage) :



    def add_to_cart(self):
        self.click((By.LINK_TEXT, "Add to cart"))   

 

    
