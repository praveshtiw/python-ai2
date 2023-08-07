from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def create_test_cases_from_url(url):
    try:
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')  # Replace with the path to your ChromeDriver executable
        driver.get(url)

        # Wait for the page to load (you might need to adjust the wait time based on the website)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Use Selenium to interact with the website and extract test case information
        test_cases = []
        # Replace the following lines with your Selenium code to extract test cases
        # For demonstration purposes, we assume test cases are extracted from <div> elements with 'test-case' class
        test_case_elements = driver.find_elements_by_class_name('test-case')
        for element in test_case_elements:
            test_case = {
                "Test Case": element.get_attribute('data-test-case'),
                "Test Scenario": element.get_attribute('data-test-scenario'),
                "Test Steps": element.get_attribute('data-test-steps'),
                "Expected Result": element.get_attribute('data-expected-result'),
                "Status": "Not Run"
            }
            test_cases.append(test_case)

        return test_cases
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

    return []

def export_to_excel(test_cases, output_file="test_cases.xlsx"):
    if not test_cases:
        print("No test cases found.")
        return

    df = pd.DataFrame(test_cases)
    try:
        df.to_excel(output_file, index=False)
        print(f"Test cases exported to {output_file}")
    except Exception as e:
        print(f"Error exporting test cases to Excel: {e}")

if __name__ == "__main__":
    # Replace "https://your_website_url" with the actual URL of the website you want to create test cases from
    website_url = "https://24livehosts.com/grocery_app/admin/"

    test_cases = create_test_cases_from_url(website_url)
    export_to_excel(test_cases)
