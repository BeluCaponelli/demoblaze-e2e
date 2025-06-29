from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    Login_button = (By.ID, "login2")
    username_input = (By.ID, "loginusername")
    password_input = (By.ID, "loginpassword")
    submit_button = (By.XPATH, "//button[text()='Log in']")
    logout_button = (By.ID, "logout2")
    login_button = (By.ID, "login2")

    def open_login_modal(self):
        self.click(self.Login_button)

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.submit_button)

    def is_logged_in(self):
        return self.wait_for_element(self.logout_button)

    def open_login_modal(self):
        self.click(self.login_button)

  