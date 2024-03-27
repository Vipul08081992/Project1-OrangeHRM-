import time
from resourses.constants.urls_portal import login_page_url,reset_page_url,dashboard_page_url,pim_page_url
from resourses.pages.Login_page import Login_page
from resourses.pages.Dashboard_page import Dashboard_page
from resourses.pages.Reset_password_page import Reset_Password
from utils.Waits import explicit_waits

def test_admin_text(open_website):
    driver=open_website
    loginpage = Login_page(driver)
    loginpage.open_dasboard(username="Admin", password="admin123")
    time.sleep(5)
    dashboard=Dashboard_page(driver)
    dashboard.click_on_PIM()
    time.sleep(3)
    url=driver.current_url
    assert url == pim_page_url()

