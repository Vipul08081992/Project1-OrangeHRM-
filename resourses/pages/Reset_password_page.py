from selenium.webdriver.common.by import By
class Reset_Password:
    def __init__(self,driver):
        self.driver=driver
    username=(By.CLASS_NAME,"oxd-input oxd-input--active")
    blank_user_error=(By.CLASS_NAME,"oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message")
    cancel=(By.CLASS_NAME,"oxd-button oxd-button--large oxd-button--ghost orangehrm-forgot-password-button orangehrm-forgot-password-button--cancel")
    reset=(By.CLASS_NAME,"oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset")
    heading_box=(By.CLASS_NAME,"oxd-text oxd-text--h6 orangehrm-forgot-password-title")
    def get_username(self):
        return self.driver.find_element(*self.username)
    def get_blank_username_error(self):
        return self.driver.find_element(*self.blank_user_error)
    def get_cancel_button(self):
        return self.driver.find_element(*self.cancel)
    def get_reset_button(self):
        return self.driver.find_element(*self.reset)
    def get_heading_of_resetpage(self):
        return self.driver.find_element(*self.heading_box)

#Actions on page:
    def fill_username(self,username):
        self.get_username().send_keys(username)
    def click_on_cancel_button(self):
        self.get_cancel_button().click()
    def click_on_reset_button(self):
        self.get_reset_button().click()
    def send_reset_password_link(self,username):
        self.get_username().send_keys(username)
        self.get_reset_button().click()
    def heading_of_box(self):
        return self.get_heading_of_resetpage().text

