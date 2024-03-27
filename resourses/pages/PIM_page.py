from selenium.webdriver.common.by import By
class PIM_page:
    def __init__(self,driver):
        self.driver=driver
    heading=(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
#Navigation bar
    Configuration=(By.LINK_TEXT,"Configuration ")
    EmployeeList=(By.LINK_TEXT,"Employee List")
    AddEmployee=(By.LINK_TEXT,"Add Employee")
    Reports=(By.LINK_TEXT,"Reports")
    help=(By.XPATH,"//i[@class='oxd-icon bi-question-lg']")
    
