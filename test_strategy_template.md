# 🧪 Test Strategy Template

## 🎯 Objective
Briefly describe the goal of testing for this project or feature.  
_Example: Ensure the login form is robust across valid and invalid inputs._

---

## 🧩 Scope
What parts of the product are being tested in this phase?

- Login form functionality
- Error message handling
- Field validation
- Basic front-end performance

---

## 🚫 Out of Scope
What is explicitly **not** covered?

- Backend API response testing
- Localization
- Browser/device matrix beyond Chrome (unless stated)

---

## 🧪 Test Types
Types of testing included in this plan:

- Functional Testing
- Negative Testing
- Regression Testing
- Exploratory Testing

---

## 🛠 Tooling
- Python 3
- Selenium
- ChromeDriver
- Git/GitHub for version control

---

## 🧮 Environments
- Environment: https://practicetestautomation.com/practice-test-login/
- Browser: Google Chrome (macOS)

---

## 📈 Success Criteria
- All test cases pass for valid input
- Errors are shown for invalid input
- Page behavior is consistent and predictable

---

## 🔥 Risks
- The test environment is public and may be updated without notice
- ChromeDriver or Selenium version mismatches may block execution

---

## 📊 Metrics (Optional)
- % of test cases passed
- Number of regression bugs caught
- Test run duration
