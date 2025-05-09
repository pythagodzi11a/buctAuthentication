from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

OPTIONS = Options()

def init_driver():
    # 禁用沙盒模式
    OPTIONS.add_argument('--no-sandbox')
    # 禁用GPU加速
    OPTIONS.add_argument('--disable-gpu')
    # 保持浏览器打开状态
    OPTIONS.add_experimental_option('detach', True)

    driver = webdriver.Edge(options=OPTIONS,service=Service('edgedriver\\msedgedriver.exe'))

    return driver

driver = init_driver()

# driver.get("https://www.baidu.com/")

driver.get("https://tree.buct.edu.cn/")

# time.sleep(5)

driver.implicitly_wait(10)
driver.find_element(By.XPATH,'/html/body/main/section/div[1]/div[2]/input').send_keys('Replace with your ID')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('Replace with your password')
driver.find_element(By.XPATH,'/html/body               /main/section/div[1]/div[8]/button[1]').click()
# driver.find_element(By.XPATH,'/html/body/main/section/div[1]/div[7]/button[2]').click()

# driver.find_elements(By.ID,'kw')
# 找到多个元素

# driver.find_element(By.ID,'kw').send_keys("selenium")
# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input').click()
# # 网页截图（浏览器截图）
# driver.get_screenshot_as_file("baidu.png")
# driver.refresh()
# time.sleep(2)
