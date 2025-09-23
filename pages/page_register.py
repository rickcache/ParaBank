from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Register:
    def __init__(self, driver):
        
        self.driver = driver
        self.firstName = (By.ID, "customer.firstName")
        self.lastName  = (By.ID, "customer.lastName")
        self.Address   = (By.ID, "customer.address.street")
        self.city      = (By.ID, "customer.address.city")
        self.state     = (By.ID, "customer.address.state")
        self.zip       = (By.ID, "customer.address.zipCode")
        self.phone     = (By.ID, "customer.phoneNumber")
        self.SSN       = (By.ID, "customer.ssn")
        self.username  = (By.ID, "customer.username")
        self.password  = (By.ID, "customer.password")
        self.confirm_ps = (By.ID, "repeatedPassword")
        self.registerbutton = (By.CSS_SELECTOR, "input.button[type='submit'][value='Register']" )
    
    def enter_firstname(self, firstName):
        firstName_enter =self.driver.find_element(*self.firstName)
        firstName_enter.clear()
        firstName_enter.send_keys(firstName)
        
    def enter_lastname(self, lastName):
        lastName_enter =self.driver.find_element(*self.lastName)
        lastName_enter.clear()
        lastName_enter.send_keys(lastName)
        
    def enter_Address(self, Address):
        Address_enter =self.driver.find_element(*self.Address)
        Address_enter.clear()
        Address_enter.send_keys(Address)
        
    def enter_city(self, city):
        city_enter =self.driver.find_element(*self.city)
        city_enter.clear()
        city_enter.send_keys(city)
    
    def enter_state(self, state):
        state_enter =self.driver.find_element(*self.state)
        state_enter.clear()
        state_enter.send_keys(state)
        
    def enter_zip_code(self, zip):
        zip_enter =self.driver.find_element(*self.zip)
        zip_enter.clear()
        zip_enter.send_keys(zip)
    
    def enter_phone(self, phone):
        phone_enter =self.driver.find_element(*self.phone)
        phone_enter.clear()
        phone_enter.send_keys(phone)
    
    def enter_SSN(self, SSN):
        ssn_enter =self.driver.find_element(*self.SSN)
        ssn_enter.clear()
        ssn_enter.send_keys(SSN)
    
    def enter_username(self, username):
        username_enter =self.driver.find_element(*self.username)
        username_enter.clear()
        username_enter.send_keys(username)
        
    def enter_password(self, password):
        password_enter =self.driver.find_element(*self.password)
        password_enter.clear()
        password_enter.send_keys(password)
        
    def enter_password_again(self, confirm_ps):
        confirm_enter =self.driver.find_element(*self.confirm_ps)
        confirm_enter.clear()
        confirm_enter.send_keys(confirm_ps)        
                               
    def click_register_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.registerbutton)).click()                       
        
                                       