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



# test increment button
increment = driver.find_element(By.ID, "incrementor")
increment.click()
time.sleep(3)
incremented_value = driver.find_element(By.CLASS_NAME, "odometer-digit").text
print(f"incremented counter value:{incremented_value}")
assert incremented_value == "1", "increment button did not work correctly!"

# test decrement button
increment = driver.find_element(By.ID, "decrementor")
increment.click()
time.sleep(3)
incremented_value = driver.find_element(By.CLASS_NAME, "odometer-digit").text
print(f"decremented counter value:{incremented_value}")
assert incremented_value == "0", "decrement button did not work correctly!"

# test reset button
reset_button = driver.find_element(By.ID, "resetter")
reset_button.click()
Alert(driver).accept()
time.sleep(1)
last_value = driver.find_element(By.CLASS_NAME, "odometer").text

assert last_value == "0", "Reset button doesn't work correctly!"

# Test some of the selections
select = Select(driver.find_element(By.CLASS_NAME,"select.header-element"))

select.select_by_index(1)
time.sleep(1)
increment = driver.find_element(By.ID, "incrementor")
increment.click()
time.sleep(5)
incremented_values = driver.find_elements(By.CLASS_NAME, "odometer-digit")
value = "".join([digit.text for digit in incremented_values])
assert value == "50", "selecting 50+ increment button did not work correctly!"

select.select_by_value("9")
time.sleep(3)
increment = driver.find_element(By.ID, "incrementor")
increment.click()
time.sleep(5)
incremented_values = driver.find_elements(By.CLASS_NAME, "odometer-digit")
value = "".join([digit.text for digit in incremented_values])
assert value == "59", "selecting 9+ increment button did not work correctly!"

select.select_by_visible_text("+7")
time.sleep(3)
increment = driver.find_element(By.ID, "incrementor")
increment.click()
time.sleep(5)
incremented_values = driver.find_elements(By.CLASS_NAME, "odometer-digit")
value = "".join([digit.text for digit in incremented_values])
assert value == "66", "selecting 7+ increment button did not work correctly!"
time.sleep(3)

driver.quit()
