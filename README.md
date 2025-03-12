# Selenium Automation Tests

## **Project Overview**
This project automates the testing of login functionality, adding/removing items to/from the cart, and completing a checkout process on a web application using Selenium with Python and Pytest.

## **Prerequisites**
Ensure the following are installed on your system before running the tests:

1. **Python (3.7 or later)**
2. **Google Chrome Browser**
   - Ensure you have an updated version of Chrome.
   
3. **ChromeDriver (compatible with your Chrome version)**
   - Download from: [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Add ChromeDriver to your system `PATH`.

4. **Install Required Python Packages**
   - Navigate to the project folder and install dependencies:
     ```sh
     pip install -r requirements.txt
     ```

## **How to Run the Tests**

1. **Navigate to the Project Directory**
```sh
cd path/to/Syfe_QA_Assignment
```
2. Run All Tests
To execute all test cases, run:
```sh
pytest tests/
```
3. Run a Specific Test File
To run only the login tests, use:
```sh
pytest tests/test_login.py
```
4. Run Tests with Detailed Output
For more detailed output, add the -v (verbose) flag:
```sh
pytest -v
```
## **Assumptions & Observations**

### **Assumptions**
- The website is working and can be accessed without issues.  
- The login details (username and password) are correct.  
- The test scripts assume the user is **not already logged in** before running.  
- The buttons, text fields, and other elements are **available and clickable**.  
- The **cart updates correctly** when items are added or removed.  
- The **Chrome browser and ChromeDriver are compatible** and up to date.  

---

### **Observations**
- Sometimes, the page **loads slowly**, causing buttons to not work right away. A small wait time (`time.sleep(1)`) helps.  
- The cart icon does not always update instantly. Adding a small wait (`driver.implicitly_wait(3)`) fixes this.  
- If tests fail randomly, **clearing browser cache** or using **incognito mode** can help.  
- Slow internet or website issues may cause errors. Using **explicit waits (`WebDriverWait`)** helps the script wait properly.  
- Running tests **without opening the browser (headless mode)** makes them faster but might cause failures.  
