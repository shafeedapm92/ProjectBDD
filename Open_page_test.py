from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver (make sure chromedriver is installed and in your PATH)
driver = webdriver.Chrome()

try:
    # Open the W3Schools homepage
    driver.get("https://www.w3schools.com/")
    time.sleep(2)  # Wait for page to load

finally:
    driver.quit()
