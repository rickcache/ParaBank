import pytest
from pages.page_login import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from file_data_loader import DataLoad
import logging

@pytest.mark.order(6)
@pytest.mark.account_overview 
@pytest.mark.parametrize(
    "username, password", 
    DataLoad().json_load_login("data/data_login.json")
    )    
def test_account_overview(driver, username, password): 
    login = LoginPage(driver)

    logging.info("Opening Parabank Website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm") 
    
    logging.info("Entering username and password")
    login.enter_username(username)
    login.enter_password(password)

    logging.info("Clicking login button")
    login.click_login()
            
    target = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Accounts Overview")))
    target.click()
    expected_test = "Accounts Overview"
    
    logging.info("Verifying account overview success")
    assert expected_test in driver.page_source
    logging.info("Account Overview test passed")
    