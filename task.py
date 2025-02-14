from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("https://www.tasbih.org")

#initial value check
initial_value = driver.find_element(By.CLASS_NAME, "odometer-digit").text
print(f"initial value is {initial_value}")
assert initial_value == "0", "initial counter value is not 0"

select = Select(driver.find_element(By.CLASS_NAME,"select.header-element"))

select.select_by_index(1)
time.sleep(1)
select.select_by_value("9")
time.sleep(1)
select.select_by_visible_text("+7")
time.sleep(1)

increment = driver.find_element(By.ID, "incrementor")
increment.click()

reset_button = driver.find_element(By.ID, "resetter")
reset_button.click()

Alert(driver).accept()

time.sleep(2)
driver.quit()

