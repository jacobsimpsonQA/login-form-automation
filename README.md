# Login Form Automation

## Overview
This is a beginner-friendly Selenium test using Python.  
It opens a demo login page, enters test credentials, and verifies successful login.

## Tools Used
- Python 3
- Selenium
- ChromeDriver (macOS)

## How to Run
1. Clone this repo  
2. Install dependencies:  
   ```bash
   pip3 install selenium
   ```
3. Run one of the test files:
   ```bash
   python3 test_login.py
   python3 test_failed_login.py
   python3 test_blank_login.py
   ```

## ✅ Tests Included

- `test_login_suite.py`: Unified test suite that runs all three scenarios below:
  - `test_valid_login()`: Valid login using correct credentials
  - `test_invalid_password()`: Login attempt with incorrect password
  - `test_blank_login()`: Login attempt with empty username and password fields
  - `test_empty_password.py`: Valid username with empty password, expects password validation error
  - `test_empty_username.py`: Login attempt with valid password and blank username, expects username error



(You can still run the individual test files if preferred.)

## 📘 What I’ve Learned

- How to write and organize UI automation scripts using Python and Selenium
- How to handle edge cases like invalid credentials and empty input fields
- How to use assertions to validate expected vs. actual outcomes
- How to create reusable functions for cleaner, scalable test code
- How to structure a basic QA test suite using standalone scripts
- How to push, document, and share code publicly using Git and GitHub


## Author
Jacob Simpson – QA Engineer  
[github.com/jacobsimpsonQA](https://github.com/jacobsimpsonQA)
