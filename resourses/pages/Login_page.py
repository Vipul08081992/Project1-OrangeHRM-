from selenium.webdriver.common.by import By


# Login page Elements:
class Login_element():
    def __init__(self,driver):
        self.driver=driver
    username=(By.ID,'username')
    password=(By.ID,'password')
    eye_button=(By.ID,'togglePassword')
#Location for this session:
    Inpatient_Ward=(By.ID,'Inpatient Ward')
    Isolation_Ward=(By.ID,'Isolation Ward')
    Laboratory=(By.ID,'Laboratory')
    Outpatient_Clinic=(By.ID,'Outpatient Clinic')
    Pharmacy=(By.ID,'Pharmacy')
    Registration_Desk=(By.ID,'Registration Desk')
#Login button:
    login_button=(By.ID,'loginButton')
    cannot_login=(By.ID,'cantLogin')
    
#Find Elements:
    def get_username(self):
        return self.driver.find_element(*Login_element.username)
    def get_password(self):
        return self.driver.find_element(*Login_element.password)
    

