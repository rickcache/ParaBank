import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class NewAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.account_type_dropdown = (By.ID, "type")
        self.from_account_dropdown = (By.ID, "fromAccountId")
        self.open_button_locator = (By.XPATH, '//*[@id="openAccountForm"]/form/div/input')

    def select_account_type(self, account_type):
        """Select CHECKING or SAVINGS"""
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.account_type_dropdown)
        )
        select = Select(dropdown)
        select.select_by_visible_text(account_type)

    def select_from_existing_account(self):
        """Pick the first available existing account"""
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.from_account_dropdown)
        )

        # Wait until at least 1 option is present
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_element(*self.from_account_dropdown).find_elements(By.TAG_NAME, "option")) > 0
        )

        select = Select(dropdown)
        select.select_by_index(0)  # pick first available account

    def click_open(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.open_button_locator)
        )
        button.click()
