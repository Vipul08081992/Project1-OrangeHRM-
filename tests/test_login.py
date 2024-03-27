import time
from resourses.constants.urls_portal import login_page_url,reset_page_url,dashboard_page_url
from resourses.pages.Login_page import Login_page
from resourses.pages.Reset_password_page import Reset_Password
from utils.Waits import explicit_waits


def test_login(open_website):
    driver=open_website
    loginpage=Login_page(driver)
    loginpage.open_dasboard(username="Admin",password="admin123")
    time.sleep(5)
    assert driver.current_url == dashboard_page_url()



def test_open_reset_password(open_website):
    driver=open_website
    loginpage=Login_page(driver)
    loginpage.open_forget_password_page()
    resetpage=Reset_Password(driver)
    explicit_waits(driver,5,resetpage.reset)
    url=driver.current_url
    print(url)
    assert url== reset_page_url()

