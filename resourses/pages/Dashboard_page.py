from selenium.webdriver.common.by import By
class Dashboard_page:
    def __init__(self,driver):
        self.driver=driver
    dash_heading=(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
#Side Panel Elements:
    side_panel_heading=(By.XPATH,"//nav[@class='oxd-navbar-nav']//div[@class='oxd-sidepanel-header']")
    search=(By.XPATH,"//input[@class='oxd-input oxd-input--active']")
    admin=(By.LINK_TEXT,"Admin")
    PIM=(By.LINK_TEXT,"PIM")
    Leave=(By.LINK_TEXT,"Leave")
    Time=(By.LINK_TEXT,"Time")
    Recruitment=(By.LINK_TEXT,"Recruitment")
    MyInfo=(By.LINK_TEXT,"My Info")
    Performance=(By.LINK_TEXT,"Performance")
    Dashboard=(By.LINK_TEXT,"Dashboard")
    Directory=(By.LINK_TEXT,"Directory")
    Maintenance=(By.LINK_TEXT,"Maintenance")
    Claim=(By.LINK_TEXT,"Claim")
    Buzz=(By.LINK_TEXT,"Buzz")
    def get_admin(self):
        return self.driver.find_element(*self.admin)
    def get_PIM(self):
        return self.driver.find_element(*self.PIM)

    def get_text(self):
        return self.get_admin().text
    def click_on_PIM(self):
        self.get_PIM().click()



