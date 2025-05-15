from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-data-dir=/tmp/chrome-user-data")

# Path to your local ChromeDriver
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

def login(username, password):
    # Load the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter credentials
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Click submit
    driver.find_element(By.ID, "submit").click()

    # Pause briefly for results to load
    time.sleep(2)

# Run test with valid credentials
login("student", "Password123")

# Validate that login succeeded
assert "Logged In Successfully" in driver.page_source
print("✅ Valid login test passed")

driver.quit()
