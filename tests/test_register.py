import pytest
from file_data_loader import DataLoad
from pages.page_register import Register
from selenium.webdriver.common.by import By
import logging

@pytest.mark.registration
@pytest.mark.parametrize(
    "firstname,lastname,address, city,state,zip,phone,ssn,username,password,c_ps",
    DataLoad().json_load_regi("data/data_register.json")
)

def test_registration(driver, firstname, lastname, address, city, state, zip, phone, ssn, username, password, c_ps ):
    register_page = Register(driver)
    
    logging.info("Opening Parabank Website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    
    driver.find_element(By.LINK_TEXT, "Register").click()

    logging.info("Filling form for registering test")
    register_page.enter_firstname(firstname)
    register_page.enter_lastname(lastname)
    register_page.enter_Address(address)
    register_page.enter_city(city)
    register_page.enter_state(state)
    register_page.enter_zip_code(zip)
    register_page.enter_phone(phone)
    register_page.enter_SSN(ssn)
    
    logging.info("Entering username and password")
    register_page.enter_username(username)
    register_page.enter_password(password)
    register_page.enter_password_again(c_ps)
    
    logging.info("Clicking registering")
    register_page.click_register_button()
    
    expected_text = "Your account was created successfully. You are now logged in."
    
    logging.info("Verifying registering test success")
    assert expected_text in driver.page_source
    logging.info("Register test passed")