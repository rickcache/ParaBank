from selenium.webdriver.common.by import By


class ContactUpdate:
    
    def __init__(self, driver):
        
        self.driver = driver
        self.firstName       = (By.NAME, "customer.firstName")
        self.lastName        = (By.NAME, "customer.lastName")
        self.address         = (By.NAME, "customer.address.street")
        self.city            = (By.NAME, "customer.address.city")
        self.state           = (By.NAME, "customer.address.state")
        self.zip             = (By.NAME, "customer.address.zipCode")
        self.phone           = (By.NAME, "customer.phoneNumber")
        self.button          = (By.XPATH, '//*[@id="updateProfileForm"]/form/table/tbody/tr[8]/td[2]/input') 
        
    #firstname
    def enter_firstName(self, fn):
        pn = self.driver.find_element(*self.firstName)
        pn.clear()
        pn.send_keys(fn)
    
    #lastname    
    def enter_lastName(self, ln):
        pn = self.driver.find_element(*self.lastName)
        pn.clear()
        pn.send_keys(ln)    
    
    #Address(Address, City, State)    
    def enter_address(self, paddress, pcity, pstate):
        a = self.driver.find_element(*self.address)
        c = self.driver.find_element(*self.city)
        s = self.driver.find_element(*self.state)
        
        a.clear()
        a.send_keys(paddress)
        
        c.clear()
        c.send_keys(pcity)
        
        s.clear()    
        s.send_keys(pstate)
    
    #Zip    
    def enter_zip_code(self, zip_no):
        z= self.driver.find_element(*self.zip)
        z.clear()
        z.send_keys(zip_no)
        
    #phone    
    def enter_phone(self, phNo):
        p = self.driver.find_element(*self.phone)
        p.clear()
        p.send_keys(phNo)
        
    #button
    def update_profile(self):
        button = self.driver.find_element(*self.button)
        button.click()
