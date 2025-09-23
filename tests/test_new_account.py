import pytest
from selenium.webdriver.common.by import By
from pages.page_login import LoginPage
from pages.page_open_new_account import NewAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

url = "https://parabank.parasoft.com/parabank/index.htm"
expected_text = "Account Opened!"

def open_new_account_page(driver):
    site_map = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Site Map"))
    )
    site_map.click()

    open_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Open New Account"))
    )
    open_account.click()

@pytest.mark.new_account
def test_create_checking_account(driver):
    login = LoginPage(driver)
    page = NewAccountPage(driver)
    
    logging.info("Opening Parabank website")
    driver.get(url)
    
    logging.info("Entering username and password")
    login.enter_username("BOB")
    login.enter_password("OKOKOK")
    logging.info("Clicking login button")
    login.click_login()

    logging.info("Opening new button")
    open_new_account_page(driver)
    page.select_account_type("CHECKING")
    page.select_from_existing_account()
    
    logging.info("Clicking open button")
    page.click_open()
    
    logging.info("Verifying New account success")
    assert expected_text in driver.page_source
    logging.info("New account test passed") 
     
@pytest.mark.new_account
def test_create_savings_account(driver):
    login = LoginPage(driver)
    page = NewAccountPage(driver)
    
    logging.info("Opening Parabank website")
    driver.get(url)
    
    logging.info("Entering username and password")
    login.enter_username("BOB")
    login.enter_password("OKOKOK")
    logging.info("Clicking login button")
    login.click_login()

    open_new_account_page(driver)
    page.select_account_type("SAVINGS")
    page.select_from_existing_account()
    page.click_open()
    
    logging.info("Verifying New account success")
    assert expected_text in driver.page_source
    logging.info("New account test passed")