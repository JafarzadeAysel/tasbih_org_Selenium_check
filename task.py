from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.tasbih.org")
select = Select(driver.find_element(By.CLASS_NAME,"select.header-element"))
select.select_by_index(1)
time.sleep(2)
select.select_by_value("9")
time.sleep(2)
