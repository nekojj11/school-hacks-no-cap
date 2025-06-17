from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome WebDriver (make sure chromedriver is installed and in PATH)
options = Options()
options.add_argument("--headless")  # Run browser in headless mode

service = Service('/path/to/chromedriver')  # Update path accordingly
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.blooket.com/")
    time.sleep(3)  # Wait for page to load

    # Example: Find and print the title
    print("Page title:", driver.title)

    # Add more automation steps here (login, navigate, etc.)

finally:
    driver.quit()
