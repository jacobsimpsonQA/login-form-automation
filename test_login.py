from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options to fix DevToolsActivePort issue
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-blink-features=AutomationControlled")

# Optional: use a custom user data dir to avoid macOS blocking
options.add_argument("--user-data-dir=/tmp/chrome-user-data")

# Launch Chrome with the correct service and options
service = Service("/usr/local/bin/chromedriver")  # path to your chromedriver
driver = webdriver.Chrome(service=service, options=options)

# Test login automation
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

time.sleep(2)

assert "Logged In Successfully" in driver.page_source

driver.quit()
