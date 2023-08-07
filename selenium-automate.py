from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path to chromedriver
chromedriver_path = "/snap/chromium/2529/usr/lib/chromium-browser/chromedriver"

# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path=chromedriver_path)

try:
    # Open a web page
    driver.get("https://skfinance.host4india.in/login")

    # Find an input field and fill it out
    input_field = driver.find_element_by_name("email")
    input_field.send_keys("superadmin@gmail.com")

    # Find a password field and fill it out
    password_field = driver.find_element_by_name("password")
    password_field.send_keys("Admin@123")

    # Submit the form
    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

    # Wait for a few seconds to see the result
    driver.implicitly_wait(5)

    # Print the page title
    print("Page title:", driver.title)
except Exception as e:
    print("Error:", e)
finally:
    # Close the browser
    driver.quit()
