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
- `test_login.py`: Valid login using correct credentials  
- `test_failed_login.py`: Login attempt with incorrect password, expects error message  
- `test_blank_login.py`: Submits blank username and password fields, expects validation error

## Author
Jacob Simpson – QA Engineer  
[github.com/jacobsimpsonQA](https://github.com/jacobsimpsonQA)
