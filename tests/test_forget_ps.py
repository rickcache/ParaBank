import pytest
from selenium.webdriver.common.by import By
from file_data_loader import DataLoad
from pages.page_forget_ps import Forget_Password
from pages.page_login import LoginPage
import logging

@pytest.mark.forget_ps
@pytest.mark.parametrize(
    "firstname,lastname,address,city,state,zip,ssn",
    DataLoad().json_load_forget("data/data_forget.json")
)

def test_forget_ps(driver,firstname,lastname,address,city,state,zip,ssn):
    forget_password = Forget_Password(driver)
    
    logging.info("Opening Parabank Website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    
    driver.find_element(By.LINK_TEXT, "Forgot login info?").click()
    
    logging.info("Filling Forget password form")
    forget_password.enter_firstname(firstname)
    forget_password.enter_lastname(lastname)
    forget_password.enter_address(address)
    forget_password.enter_city(city)
    forget_password.enter_state(state)
    forget_password.enter_zip_code(zip)
    forget_password.enter_ssn(ssn)
    forget_password.click_forgot()
    
    expected_message = "Your login information was located successfully. You are now logged in."
    
    logging.info("Verifing forget pasword success")
    assert expected_message in driver.page_source
    logging.info("Forget password test passed")
    