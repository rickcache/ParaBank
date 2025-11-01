import pytest
from selenium.webdriver.common.by import By
from pages.page_login import LoginPage
from pages.page_open_new_account import NewAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from file_data_loader import DataLoad
import logging

@pytest.mark.order(5)
@pytest.mark.new
@pytest.mark.parametrize(
    "username, password", 
    DataLoad().json_load_login("data/data_login.json")
    )    
def test_create_checking_account(driver, username, password):
    login = LoginPage(driver)
    page = NewAccountPage(driver)
    
    logging.info("Opening Parabank website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    
    logging.info("Entering username and password")
    login.enter_username(username)
    login.enter_password(password)
    logging.info("Clicking login button")
    login.click_login()
    
    logging.info("Login successful")
    
    logging.info("Opening new account")
    page.new_account()
    
    logging.info("Testing")
    expected_text = "Account Opened!" 
    assert expected_text in driver.page_source 
    logging.info("Test successful")