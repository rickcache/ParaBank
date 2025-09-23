import pytest
from pages.page_logout import LogoutPage
from pages.page_login import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
import logging

@pytest.mark.logout
def test_logout(driver):
    
    logout_page = LogoutPage(driver)
    login_page = LoginPage(driver)
    
    logging.info("Opening Parabank website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    
    logging.info("Entering username and website")
    login_page.enter_username("BOB")
    login_page.enter_password("OKOKOK")
    login_page.click_login()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "accountTable"))
    )
    
    logout_page.logout()
    
    success_logout = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginPanel"))
    )
    
    logging.info("Verifying logout success")
    assert success_logout.is_displayed()
    logging.info("Logout test passed")
