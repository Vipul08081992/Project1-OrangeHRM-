from selenium.webdriver.common.by import By
class Add_employee_page:
    def __init__(self,driver):
        self.driver=driver
    heading=(By.CLASS_NAME,"oxd-text oxd-text--h6 orangehrm-main-title")
# Full Employee Name:
    firstName=(By.NAME,"firstName")
    middleName=(By.NAME,"middleName")
    lastName=(By.NAME,"lastName")
    employeeId=(By.XPATH,"//div[@class='orangehrm-employee-container']//input[@class='oxd-input oxd-input--active']")
    add_image_button=(By.XPATH,"//i[@class='oxd-icon bi-plus']")
    added_image=(By.XPATH,"//img[@class='employee-image']")
#Create Login Details:
    create_login_details=(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")

#Save and Cancel button:
    cancel=(By.LINK_TEXT," Cancel ")
    save=(By.LINK_TEXT," Save ")

