from selenium.webdriver.common.by import By


class BillPay:
    
    def __init__(self, driver):
        
        self.driver = driver
        self.payee_name      = (By.NAME, "payee.name")
        self.address         = (By.NAME, "payee.address.street")
        self.city            = (By.NAME, "payee.address.city")
        self.state           = (By.NAME, "payee.address.state")
        self.zip             = (By.NAME, "payee.address.zipCode")
        self.phoneNO         = (By.NAME, "payee.phoneNumber")
        self.accountNO       = (By.NAME, "payee.accountNumber")
        self.accountNOVerify = (By.NAME, "verifyAccount")
        self.amount          = (By.NAME, "amount")
        self.button          = (By.XPATH, '//*[@id="billpayForm"]/form/table/tbody/tr[14]/td[2]/input')
        self.target_link     = (By.LINK_TEXT, "Bill Pay")
        
        
    def target_link(self):
        t= self.driver.find_element(*self.target_link)
        t.click()
            
    def enter_payee_name(self, name):
        pn = self.driver.find_element(*self.payee_name)
        pn.clear()
        pn.send_keys(name)
        
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
        
    def enter_zip_code(self, zip_no):
        z= self.driver.find_element(*self.zip)
        z.clear()
        z.send_keys(zip_no)
        
    def enter_phone(self, phNo):
        p = self.driver.find_element(*self.phoneNO)
        p.clear()
        p.send_keys(phNo)
        
    def enter_AccountNo(self, accNo):
        a = self.driver.find_element(*self.accountNO)
        a.clear()
        a.send_keys(accNo)
        
    def enter_verify_accountNo(self, VaccNo):
        v = self.driver.find_element(*self.accountNOVerify)
        v.clear()
        v.send_keys(VaccNo) 
        
    def enter_ammount(self, value):
        ea = self.driver.find_element(*self.amount) 
        ea.clear()
        ea.send_keys(value) 
    
    def send_payment(self):
        button = self.driver.find_element(*self.button)
        button.click()            
                