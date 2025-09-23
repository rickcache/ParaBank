from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class TransferFunds:
    def __init__(self, driver):
        self.driver = driver
        self.amount_input = (By.ID, "amount")
        self.from_account_dropdown = (By.ID, "fromAccountId")
        self.to_account_dropdown = (By.ID, "toAccountId")
        self.transfer_button = (By.XPATH, '//*[@id="transferForm"]/div[2]/input')

    def enter_amount(self, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.amount_input)
        )
        element.clear()
        element.send_keys(str(value))

    def select_from_account(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_account_dropdown)
        )
        select = Select(dropdown)
        select.select_by_value("13899")  # string

    def select_to_account(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.to_account_dropdown)
        )
        select = Select(dropdown)
        select.select_by_value("13899")  # string

    def click_transfer(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.transfer_button)
        )
        button.click()
