from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.logout_button = (By.LINK_TEXT, "Log Out")
        
    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()
