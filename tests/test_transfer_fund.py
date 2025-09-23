import pytest
from pages.page_login import LoginPage
from pages.page_fund_transfer import TransferFunds
from selenium.webdriver.common.by import By
import logging


@pytest.mark.fund_transfer
def test_fund_transfer(driver):
     
    login = LoginPage(driver)
    
    logging.info("Opening Parabank website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")     
    
    logging.info("Entering username and password")
    login.enter_username("BOB")
    login.enter_password("OKOKOK")
    logging.info("Clicking login button")
    login.click_login()
    
    
    transfer_funds= driver.find_element(By.LINK_TEXT, "Transfer Funds")
    transfer_funds.click()
    
    logging.info("Entering transfer amount")
    transfer = TransferFunds(driver)
    transfer.enter_amount("500")
    logging.info("Clicking Transfer button")
    transfer.click_transfer()
    
    
    expected_text = "Transfer Complete!"
    
    logging.info("Verifing transfer fund success")
    assert expected_text in driver.page_source
    logging.info("Transfer fund test passed")

    