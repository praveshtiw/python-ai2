from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def send_gmail(gmail_username, gmail_password, to_email, subject, message):
    # Set the path to chromedriver
    chromedriver_path = "/usr/bin/chromedriver"

    # Initialize Chrome WebDriver with options
    service = Service(executable_path=chromedriver_path)
    options = webdriver.ChromeOptions()

    #Uncomment the following line if you want to run Chrome in headless mode (without GUI)
    # options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open Gmail login page
        driver.get("https://accounts.google.com/ServiceLogin")

        # Fill in the username and click "Next"
        email_input = driver.find_element("name", "identifier")
        email_input.send_keys(gmail_username)
        email_input.send_keys(Keys.RETURN)

        time.sleep(5)  # Wait for the next page to load

        # Fill in the password and click "Next"
        password_input = driver.find_element("name", "Passwd")
        password_input.send_keys(gmail_password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(5)  # Wait for the Gmail inbox to load

        # Compose a new email
        driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")

        time.sleep(2)  # Wait for the new email window to load

        # Fill in the recipient, subject, and message
        recipient_input = driver.find_element_by_name("to")
        recipient_input.send_keys(to_email)

        subject_input = driver.find_element_by_name("subjectbox")
        subject_input.send_keys(subject)

        message_input = driver.find_element_by_css_selector("div[role='textbox']")
        message_input.send_keys(message)

        # Send the email
        send_button = driver.find_element_by_css_selector("div[data-tooltip='Send ‪(Ctrl-Enter)‬']")
        send_button.click()

        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    gmail_username = "praveshtiwari.dev@gmail.com"
    gmail_password = "W3care#!@#$"
    to_email = "arpit@w3care.com"
    subject = "Test Email using Bot"
    message = "Hi, this is a test mail using bot."

    send_gmail(gmail_username, gmail_password, to_email, subject, message)
