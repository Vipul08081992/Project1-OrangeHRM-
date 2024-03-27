import time

from selenium import webdriver
from resourses.constants.urls_portal import login_page_url
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get(login_page_url())
driver.maximize_window()
time.sleep(3)
forget_password_link=driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
forget_password_link.click()
time.sleep(5)
Text=driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']")
Heading=Text.text
print(Heading)
