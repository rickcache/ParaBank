
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Forget_Password():
    def __init__(self, driver):
        self.driver = driver
        self.firstname = (By.ID, "firstName")
        self.lastname  = (By.ID, "lastName")
        self.address   = (By.ID, "address.street")
        self.city      = (By.ID, "address.city")
        self.state     = (By.ID, "address.state")
        self.zip       = (By.ID, "address.zipCode")
        self.ssn       = (By.ID, "ssn")
        self.button    = (By.CSS_SELECTOR, "input.button[type='submit'][value='Find My Login Info']")
    
    def enter_firstname(self, firstname):
        ef = self.driver.find_element(*self.firstname)    
        ef.clear()
        ef.send_keys(firstname)
        
    def enter_lastname(self, lastname):
        el = self.driver.find_element(*self.lastname)
        el.clear()
        el.send_keys(lastname)
        
    def enter_address(self, address):
        ea = self.driver.find_element(*self.address)
        ea.clear()
        ea.send_keys(address)
        
    def enter_city(self, city):
        ec = self.driver.find_element(*self.city)
        ec.clear()
        ec.send_keys(city) 
    
    def enter_state(self, state):
        es = self.driver.find_element(*self.state)
        es.clear()
        es.send_keys(state)
        
    def enter_zip_code(self, zip):
        ez = self.driver.find_element(*self.zip)
        ez.clear()
        ez.send_keys(zip)
        
    def enter_ssn(self, ssn):
        ess= self.driver.find_element(*self.ssn)
        ess.clear()
        ess.send_keys(ssn) 
        
    def click_forgot(self):
        element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button))
        element.click()