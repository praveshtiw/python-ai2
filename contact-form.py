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
    # Open the contact page
    driver.get("https://training.host4india.in/pratyush/contact.php")

    # Find the name input field and fill it out
    name_input = driver.find_element(By.NAME, "name")
    name_input.send_keys("John Doe")

    # Find the email input field and fill it out
    email_input = driver.find_element(By.NAME, "username")
    email_input.send_keys("johndoe@example.com")

    # Find the subject input field and fill it out
    subject_input = driver.find_element(By.NAME, "subject")
    subject_input.send_keys("Test Subject")

    # Find the message input field and fill it out
    message_input = driver.find_element(By.NAME, "message")
    message_input.send_keys("This is a test message using Selenium.")
    
    driver.implicitly_wait(20)
    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Wait for a few seconds to see the result
    driver.implicitly_wait(20)

    # Print the page title
    print("Page title after submitting the form:", driver.title)

except Exception as e:
    print("Error:", e)
finally:
    # Close the browser
    driver.quit()
