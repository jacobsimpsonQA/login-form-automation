from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-data-dir=/tmp/chrome-user-data")

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://practicetestautomation.com/practice-test-login/")

# Use valid username, invalid password
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.ID, "submit").click()

time.sleep(2)

# Check for error message
error_message = driver.find_element(By.ID, "error").text
assert "Your password is invalid!" in error_message, "Failed login error not shown"

print("❌ Login correctly failed as expected")

driver.quit()
