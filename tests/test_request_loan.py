import pytest
from pages.page_login import LoginPage
from pages.page_request_loan import RequestLoan
from selenium.webdriver.common.by import By
import logging
from file_data_loader import DataLoad

@pytest.mark.order(9)
@pytest.mark.request_loan
@pytest.mark.parametrize(
    "username, password", 
    DataLoad().json_load_login("data/data_login.json")
    )    
def test_request_loan(driver, username, password):
    login = LoginPage(driver)
    request = RequestLoan(driver)
    
    logging.info("Opening Parabank website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    
    logging.info("Entering username and password")
    login.enter_username(username)
    login.enter_password(password)
    logging.info("Clicking logging button")
    login.click_login()
    
    target = driver.find_element(By.LINK_TEXT, "Request Loan")
    target.click()
    
    logging.info("Entering loan amount & down payment amoubt")
    request.enter_loan_amount("8902")
    request.enter_down_payment("909")
    logging.info("Clicking Apply Button")
    request.apply_now()
    
    expected_text = "Loan Request Processed"
    
    logging.info("Verifying loan request button")
    assert expected_text in driver.page_source
    logging.info("Loan request test passed")
    
    