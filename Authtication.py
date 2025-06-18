import os
import requests
import time
import selenium.common.exceptions
import logging
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(
    level=logging.INFO,
    format="%(levelno)s - %(levelname)s - %(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="log.log",
    filemode="a"
)

class BUCTAU:
    def __init__(self):
        load_dotenv()

        self.USER_USERNAME = os.environ.get('BUCT_AUTHENTICATION_USERNAME')
        self.USER_PASSWORD = os.environ.get('BUCT_AUTHENTICATION_PASSWORD')
        self.USER_NAME = os.getlogin()

        logging.info(f"USER now is {self.USER_NAME}")
        logging.info(f"BUCTAU initialized with username:{self.USER_USERNAME}")
        logging.info(f"BUCTAU initialized with password:{self.USER_PASSWORD}")
        # print(f"USER now is {self.USER_NAME}")
        # print("BUCTAU initialized with username:", self.USER_USERNAME)
        # print("BUCTAU initialized with password:", self.USER_PASSWORD)

    @staticmethod
    def init_driver_edge():
        """Initialize the Selenium WebDriver with Edge options.
        Returns:
            WebDriver: The initialized Selenium WebDriver instance.
        """
        from selenium.webdriver.edge.options import Options
        from selenium.webdriver.edge.service import Service

        service = Service()
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")
        # options.add_experimental_option("detach", True)
        driver = webdriver.Edge(service=service, options=options)
        driver.implicitly_wait(5)  # Implicit wait for elements to load
        return driver

    @staticmethod
    def init_driver_chrome():
        """Initialize the Selenium WebDriver with Chrome options.
        Returns:
            WebDriver: The initialized Selenium WebDriver instance.
        """
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service

        service = Service(executable_path="/usr/bin/chromedriver")
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")
        # options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(5)  # Implicit wait for elements to load
        return driver

    def login(self, driver):
        """open the page and login"""
        logging.info("LOGIN")
        driver.get("https://tree.buct.edu.cn/index_20.html")
        driver.maximize_window()
        try:
            driver.find_element(By.XPATH, '/html/body/main/section/div[1]/div[2]/input').send_keys(self.USER_USERNAME)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.USER_PASSWORD)
            driver.find_element(By.XPATH, '/html/body/main/section/div[1]/div[8]/button[1]').click()
            return True
        except selenium.common.exceptions.NoSuchElementException as e:
            logging.info("NoSuchElementException: ", e)
            return False

    @staticmethod
    def detect_net_requests():
        # noinspection PyBroadException
        try:
            detector = requests.get(url="https://www.baidu.com", timeout=5)
            if detector.status_code == 200:
                logging.info("Network is available")
                return True
            else:
                logging.info("Network is not available")
                return False
        except requests.ConnectionError:
            logging.info("ConnectionError: False")
            return False
        except Exception:
            return False

    @staticmethod
    def detect_net(driver):
        # noinspection PyBroadException
        try:
            driver.get("https://tree.buct.edu.cn/index_20.html")
            driver.maximize_window()
            time.sleep(3)  # Wait for the page to load
            driver.find_element(By.XPATH, '/html/body/main/section/div[1]/div[7]/button[1]')
            logging.info("Have logged in")
            return True  # Not logged in
        except Exception:
            logging.warning("Not logged in")
            return False
