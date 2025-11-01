import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class NewAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_account_page = (By.XPATH, '//*[@id="leftPanel"]/ul/li[1]/a')
        self.account_type_path = (By.XPATH, '//*[@id="type"]')
        self.deposit_path      = (By.XPATH, '//*[@id="fromAccountId"]')
        self.btn_path          = (By.XPATH, '//*[@id="openAccountForm"]/form/div/input')
        
    def new_account(self):
        wait = WebDriverWait(self.driver, 10)
        
        account_page = wait.until(EC.element_to_be_clickable((self.new_account_page)))
        account_page.click()
        
        wait.until(EC.url_contains("/openaccount"))
        
        dropdown_type = Select(wait.until(EC.element_to_be_clickable((self.account_type_path))))
        dropdown_type.select_by_visible_text("CHECKING")
        
        button = wait.until(EC.element_to_be_clickable((self.btn_path)))
        button.click()
        