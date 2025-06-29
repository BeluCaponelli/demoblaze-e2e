from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUpPage(BasePage):
    username_input = (By.ID, "sign-username")
    password_input = (By.ID, "sign-password")
    submit_signup_button = (By.XPATH, "//button[text()='Sign up']")
    signUp_button = (By.ID, "signin2")

    def open_signup_modal(self):
        self.click(self.signUp_button)

    def fill_signup_form(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.submit_signup_button)
       