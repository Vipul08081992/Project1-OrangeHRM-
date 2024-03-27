import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Login_page:
    def __init__(self,driver):
        self.driver=driver
    username=(By.NAME,'username')
    blank_user=(By.XPATH,"//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")
    password=(By.NAME,'password')
    blank_password=(By.XPATH,"//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]")
    login_button=(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
    error_message=(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    forget_password=(By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
#Get Elements:
    def get_username(self):
        return self.driver.find_element(*self.username)
    def get_blank_user(self):
        return self.driver.find_element(*self.blank_user)
    def get_password(self):
        return self.driver.find_element(*self.password)
    def get_blank_password(self):
        return self.driver.find_element(*self.blank_password)
    def get_login_button(self):
        return self.driver.find_element(*self.login_button)
    def get_error_message(self):
        return self.driver.find_element(*self.error_message)
    def get_forget_password(self):
        return self.driver.find_element(*self.forget_password)

# Actions of the page:
    def blank_username_error_message(self):
        return self.get_blank_user().text
    def blank_password_error_message(self):
        return self.get_blank_password().text

    def open_dasboard(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login_button().click()

    def unable_to_login_error(self):
        return self.get_error_message().text

    def open_forget_password_page(self):
        forgetpassword_link=self.get_forget_password()
        forgetpassword_link.click()



