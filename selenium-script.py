from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    driver.get("https://skfinance.host4india.in/login")

    # Wait for the email input field to be clickable and fill it out
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "email"))
    )
    email_input.send_keys("superadmin@gmail.com")

    # Wait for the password input field to be clickable and fill it out
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "password"))
    )
    password_input.send_keys("Admin@123")

    # Wait for the login button to be clickable and perform the login action
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()

    # Wait for a few seconds to see the result (you may adjust the waiting time based on the website behavior)
    driver.implicitly_wait(5)


     # Wait for the login button to be clickable and perform the login action
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='dw-menu']"))
    )
    menu_button.click()

    # Select Yard Management from the sidebar
    yard_management_sidebar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Yard Management']"))
    )
    yard_management_sidebar.click()

    # Click on Vehicle Listing
    vehicle_listing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Vehicle Listing']"))
    )
    vehicle_listing.click()

    # Click on the plus icon to add a new vehicle
    plus_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='fas fa-plus']"))
    )
    plus_icon.click()

    # Fill the form with vehicle details (assuming the fields have the appropriate names)
    vehicle_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form[@id='vehicleForm']"))
    )
    vehicle_form.find_element_by_name("vehicle_name").send_keys("Test Vehicle")
    vehicle_form.find_element_by_name("vehicle_number").send_keys("ABC123")
    vehicle_form.find_element_by_name("vehicle_type").send_keys("Car")
    # Add more fields as required

    # Submit the form
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()

    # Wait for a few seconds to see the result (you may adjust the waiting time based on the website behavior)
    driver.implicitly_wait(5)

    # Print the page title after submitting the form (you may perform further actions as needed)
    print("Page title after submitting the form:", driver.title)

    # You can perform additional actions after submitting the form, such as verifying the success message, etc.

except Exception as e:
    print("Error:", e)
finally:
    # Close the browser
    driver.quit()
