import pytest
from pages.page_login import LoginPage
from pages.page_bill_pay import BillPay
from selenium.webdriver.common.by import By
import logging

@pytest.mark.bill
def test_pay_bill(driver):
    login = LoginPage(driver)
    bill  = BillPay(driver)
    
    logging.info("Opening Parabank Website")
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    
    logging.info("Entering username and password")
    login.enter_username("BOB")
    login.enter_password("OKOKOK")
    
    logging.info("Clicking logging button")
    login.click_login()
    
    bill_pay= driver.find_element(By.LINK_TEXT, "Bill Pay")
    bill_pay.click()
   
    logging.info("Filling Form for Bill Pay")
    bill.enter_payee_name("BOB")
    bill.enter_address("11 no school road barrackpore", "Kolkata", "West Bengal")
    bill.enter_zip_code("70012W")
    bill.enter_phone("9007567325")
    bill.enter_AccountNo("13445")
    bill.enter_verify_accountNo("13445")
    bill.enter_ammount("500")
    bill.send_payment()
    
    except_text = "Bill Payment Complete"
    
    logging.info("Verifying Bill Payment test")
    assert except_text in driver.page_source
    logging.info("Bill Pay test passed")