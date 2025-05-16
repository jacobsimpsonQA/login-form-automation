from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Reusable setup
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

def test_valid_login():
    login("student", "Password123")
    assert "Logged In Successfully" in driver.page_source
    print("✅ Valid login test passed")

def test_invalid_password():
    login("student", "wrongpassword")
    error_message = driver.find_element(By.ID, "error").text
    assert "Your password is invalid!" in error_message
    print("❌ Invalid password test passed – error shown")

def test_blank_login():
    login("", "")
    error_message = driver.find_element(By.ID, "error").text
    assert "Your username is invalid!" in error_message or "Your password is invalid!" in error_message
    print("⚠️ Blank login test passed – error shown")

# Run all tests
if __name__ == "__main__":
    test_valid_login()
    test_invalid_password()
    test_blank_login()
    driver.quit()
