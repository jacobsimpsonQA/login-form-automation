from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome options setup for macOS
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-data-dir=/tmp/chrome-user-data")

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

def login(username, password):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

# Run test with valid username and empty password
login("student", "")

# Check for the correct error message
try:
    error_message = driver.find_element(By.ID, "error").text
    assert "Your password is invalid!" in error_message
    print("⚠️ Empty password test passed – correct error shown")
except:
    print("❌ Empty password test may have failed – no error message found")

driver.quit()
