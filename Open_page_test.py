from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Use webdriver-manager to handle ChromeDriver setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the W3Schools homepage
    driver.get("https://www.w3schools.com/")
    time.sleep(2)  # Wait for page to load

finally:
    driver.quit()
