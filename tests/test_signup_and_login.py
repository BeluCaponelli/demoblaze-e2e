import pytest
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.signup_page import SignUpPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage


class TestUserCreation:


    @classmethod
    def setup_class(cls):
        cls.username = f"user{random.randint(1000, 9999)}"
        cls.password = "Test123!"

    
    def test_signup_shows_success_modal(self,driver):
        wait = WebDriverWait(driver, 10)

        signUpPage = SignUpPage(driver)
        signUpPage.open_signup_modal()
        signUpPage.fill_signup_form(self.username, self.password)

        alert = wait.until(EC.alert_is_present())
        assert "Sign up successful" in alert.text
        alert.accept()

    def test_user_can_login(self, driver):      

        login = LoginPage(driver)
        login.open_login_modal()
        
        login.login(self.username, self.password)

        assert login.is_logged_in()

    def test_add_product_to_cart(self, driver):
        wait = WebDriverWait(driver, 10)

        home = HomePage(driver)
        home.select_product() 

        product = ProductPage(driver)
        product.add_to_cart()

        alert = wait.until(EC.alert_is_present())
        assert "Product added." in alert.text 
        alert.accept()
        
        cart = CartPage(driver)
        cart.open_cart()
        
        assert cart.has_products()
        
    def test_complete_purchase(self,driver):
        cart = CartPage(driver)
        cart.place_order()

        cart.fill_order_form(
        name="Test",
        country="Argentina",
        city="BsAs",
        card="1234567890",
        month="06",
        year="2025"
        )

        cart.confirm_purchase()
        assert "Thank you for your purchase!" in cart.get_success_message()
