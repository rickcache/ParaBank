import pytest
from pages.page_login import LoginPage
from pages.page_update_contact import ContactUpdate
from selenium.webdriver.common.by import By
from file_data_loader import DataLoad
import logging

@pytest.mark.order(10)
@pytest.mark.contact_update
@pytest.mark.parametrize(
    "username, password", 
    DataLoad().json_load_login("data/data_login.json")
    )    
def test_contact_update(driver, username, password):
    login = LoginPage(driver)
    update = ContactUpdate(driver)
    
    logging.info("Opening Parabank website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    
    logging.info("Entering username and password")
    login.enter_username(username)
    login.enter_password(password)
    logging.info("Clicking login button")
    login.click_login()
    
    target = driver.find_element(By.LINK_TEXT, "Update Contact Info")
    target.click()
    
    logging.info("Filling form for updating contact")
    update.enter_firstName("Bob")
    update.enter_lastName("Johnson")
    update.enter_address("789 Oak Lane", "Austin", "Texas")
    update.enter_zip_code("73301")
    update.enter_phone("02175551234")
    update.update_profile()
    
    expected_text = "Profile Updated"
    
    logging.info("Verifying Contact Update test success")
    assert expected_text in driver.page_source
    logging.info("Contact Update test passed")