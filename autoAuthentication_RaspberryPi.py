

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options

import time
import json
import logging
# import sched
# from datetime import datetime

Options = Options()

INTERVAL = 0.5 # Interval time in mins

def init_driver():
    """Initialize the Selenium WebDriver with Chrome options.
    Returns:
        WebDriver: The initialized Selenium WebDriver instance.
    """

    Options.add_argument("--headless")  # Run in headless mode

    # Options.add_argument("--user-data-dir=/home/pythagodzilla/.config/chromium/ChromeUserDataDir")
    # Options.add_argument("--incognito")  # Use incognito mode
    # Options.add_argument("--no-user-data-dir")  # Disable user data directory

    Options.add_argument("--no-sandbox")
    Options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(), options=Options)
    driver.implicitly_wait(5)  # Implicit wait for elements to load
    return driver

def login(driver):
    """This function is only used for login. Only find the elements and send keys. And do nothing else.
    Args:
        driver: The Selenium WebDriver instance.
    """
    driver.find_element(By.XPATH, '/html/body/main/section/div[1]/div[2]/input').send_keys('Replace with your ID')
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('Replace with your password')
    driver.find_element(By.XPATH,'/html/body               /main/section/div[1]/div[8]/button[1]').click()

def check_login_status(driver):
    """Check if logged in
    Args:
        driver: The Selenium WebDriver instance.
    Returns:
        bool: True if logged in, False otherwise.
    """
    driver.get("https://tree.buct.edu.cn/index_20.html")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    try:
        driver.find_element(By.XPATH, '/html/body/main/section/div[1]/div[7]/button[1]')
        # print("Have logged in")
        return True  # Not logged in
    except:
        # print("Not logged in")
        return False  # Logged in

def do_check_and_login(driver):
    """When this function is called, check first and if not logged in, login. And if logged failed, retry 10 times. And if still failed, return false. And if logged in, return true.
    Args:
        driver: The Selenium WebDriver instance.
    """
    retry_times = 0
    driver.get("https://tree.buct.edu.cn/index_20.html")
    driver.maximize_window()

    if retry_times < 10:
        if check_login_status(driver):
            # print("Already logged in")
            retry_times = 0
            return
        else:
            login(driver)

        time.sleep(3)

        if check_login_status(driver):
            # print("Login successful")
            retry_times = 0
            return
        else:
            do_check_and_login(driver)
            retry_times += 1
    else:
        # print("Login failed after 10 retries")
        return False

    # if check_login_status(driver):
    #     # print("Login successful")
    #     retry_times = 0
    # else:
    #     # print("Login failed")
    #     # print("retrying...")

    #     retry_times += 1
    #     do_login(driver, retry_times=retry_times)
    # return retry_times
    # 有时间再做sched吧

past_time = time.time()
driver = init_driver() #初始化driver
# print("Already logged in")
do_check_and_login(driver)


while True:
    if time.time() - past_time > INTERVAL * 60:
        # print("Time to login")
        if check_login_status(driver):
            past_time = time.time()
        else:
                # login_status = do_check_and_login(driver)
            do_check_and_login(driver)
            past_time = time.time()

