from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    cart_button = (By.ID, "cartur")
    place_order_button = (By.XPATH, "//button[text()='Place Order']")
    purchase_button = PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    product_rows = (By.XPATH, "//tr[contains(@class, 'success')]")
    success_message = (By.CLASS_NAME, "sweet-alert")

    name_input = (By.ID, "name")
    country_input = (By.ID, "country")
    city_input = (By.ID, "city")
    card_input = (By.ID, "card")
    month_input = (By.ID, "month")
    year_input = (By.ID, "year")
                                    
    def open_cart(self):
         self.click(self.cart_button)

    def has_products(self):
        self.wait.until(lambda d: len(d.find_elements(*self.product_rows)) > 0)
        rows = self.driver.find_elements(*self.product_rows)
        return len(rows) > 0
    
    def place_order(self):
        self.click(self.place_order_button)

    def fill_order_form(self, name, country, city, card, month, year):
        self.type(self.name_input, name)
        self.type(self.country_input, country)
        self.type(self.city_input, city)
        self.type(self.card_input, card)
        self.type(self.month_input, month)
        self.type(self.year_input, year)

    def confirm_purchase(self):
        self.click(self.purchase_button)

    def get_success_message(self):
        return self.get_text(self.success_message)