import os
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

class Authentication:
    def __init__(self):
        self.USER_ID = os.environ.get('BUCT_AUTHENTICATION_ID')
        self.USER_PASSWORD = os.environ.get('BUCT_AUTHENTICATION_PASSWORD')

    @staticmethod
    def init_driver():
        """Initialize the Selenium WebDriver with Chrome options.
        Returns:
            WebDriver: The initialized Selenium WebDriver instance.
        """
        service = Service()
        options = Options()
        # options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(service=service, options=options)
        driver.implicitly_wait(5)  # Implicit wait for elements to load
        return driver

    def login(self, driver):
        """open the page and login"""
        driver.get("https://tree.buct.edu.cn/index_20.html")
        driver.maximize_window()

        try:
            driver.find_element(By.XPATH, '/html/body/main/section/div[1]/div[2]/input').send_keys(self.USER_ID)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.USER_PASSWORD)
            driver.find_element(By.XPATH, '/html/body               /main/section/div[1]/xxxdiv[8]/button[1]').click()
            return None
        except selenium.common.exceptions.NoSuchElementException as e:
            print("NoSuchElementException: ", e)
            return None