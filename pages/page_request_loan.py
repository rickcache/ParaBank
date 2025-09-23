from selenium.webdriver.common.by import By

class RequestLoan:
    
    def __init__(self, driver):
        
        self.driver = driver
        self.loan_amount = (By.ID, "amount")
        self.down_payment = (By.ID, "downPayment")
        self.apply_button = (By.XPATH, '//*[@id="requestLoanForm"]/form/table/tbody/tr[4]/td[2]/input')
        
    def enter_loan_amount(self, amount):
        a = self.driver.find_element(*self.loan_amount)
        a.clear()
        a.send_keys(amount)
            
    def enter_down_payment(self, down):
        d = self.driver.find_element(*self.down_payment)
        d.clear()
        d.send_keys(down)
        
    def apply_now(self):
        button = self.driver.find_element(*self.apply_button)
        button.click()
                      