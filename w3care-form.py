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

    # Wait for the input fields to be clickable and fill them out
    name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "your-name"))
    )
    name_input.send_keys("John Doe")

    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "your-email"))
    )
    email_input.send_keys("johndoe@example.com")

    phone_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "your-phone"))
    )
    phone_input.send_keys("1234567890")

    # Select "United States" from the "country" dropdown
    country_dropdown = Select(driver.find_element(By.NAME, "your-country"))
    country_dropdown.select_by_visible_text("United States")

    # Select "$1000" from the "request_quote_site_budget" dropdown
    budget_dropdown = Select(driver.find_element(By.NAME, "your-budget"))
    budget_dropdown.select_by_value("USD 100 - USD 1,000")

    message_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "your-message"))
    )
    message_input.send_keys("This is a test message using Selenium.")

    # Wait for the submit button to be clickable and submit the form
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Send Message']"))
    )
    submit_button.click()

    # Wait for a few seconds to see the result (you may adjust the waiting time based on the website behavior)
    driver.implicitly_wait(15)

    # Print the page title after submitting the form (you may perform further actions as needed)
    print("Page title after submitting the form:", driver.title)

    # You can perform additional actions after submitting the form, such as verifying the success message, etc.

except WebDriverException as e:
    print("WebDriverException Error:", e)
except Exception as e:
    print("Error:", e)
finally:
    # Close the browser
    driver.quit()
