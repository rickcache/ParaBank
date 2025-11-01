import pytest
from pages.page_login import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from file_data_loader import DataLoad
import json
import logging

@pytest.mark.order(2)    
@pytest.mark.login
@pytest.mark.parametrize(
    "username, password", 
    DataLoad().json_load_login("data/data_login.json")
    )    
def test_login(driver, username, password):
    login_page = LoginPage(driver) 
    
    
    logging.info("Opening Parabank website") 
    driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
      
    logging.info("Entering username and password")
    login_page.enter_username(username)
    login_page.enter_password(password)
    logging.info("Clicking login button")
    login_page.click_login()
    
    success_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="accountTable"]')))
      
    logging.info("Verifying login success")
    assert  success_element.is_displayed()
    logging.info("Login test passed")

