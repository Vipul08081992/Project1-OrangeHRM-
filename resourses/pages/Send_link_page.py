from selenium.webdriver.common.by import By
class Send_link_page:
    def __init__(self,driver):
        self.driver=driver
    heading_box=(By.CLASS_NAME,"oxd-text oxd-text--h6 orangehrm-forgot-password-title")
    reset_text=(By.CLASS_NAME,"oxd-text oxd-text--p")
    def get_heading_of_box(self):
        return self.driver.find_element(*self.heading_box).text
    def elements_of_box(self):
        Text=[]
        Text_elements=self.driver.find_elements(*self.reset_text)
        for t in Text_elements:
            Text.append(t.text)
        return Text


