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


(You can still run the individual test files if preferred.)

## Author
Jacob Simpson – QA Engineer  
[github.com/jacobsimpsonQA](https://github.com/jacobsimpsonQA)
