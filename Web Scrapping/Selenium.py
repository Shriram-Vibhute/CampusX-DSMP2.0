from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the driver path
s = Service("C:/Users/shrir/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Setting options for web-browsers
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("start-maximized")

# Define the browser and open the window
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://google.com")
time.sleep(2)

# Finding the input element and sending the text related to our search
user_input = driver.find_element(by=By.NAME, value='q')
user_input.send_keys("CampusX")
user_input.send_keys(Keys.ENTER)
time.sleep(25) # Inserting this long enough because - Authenticating require time 
# Wait and click on the first search result
try:
    # More reliable selector using CSS
    wait = WebDriverWait(driver, 10)
    first_result = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.g a'))
    )
    first_result.click()
    
    # Wait for the page to load
    time.sleep(3)
    
    # Wait for the enroll button on the new page
    enroll_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Enroll')]"))
    )
    enroll_button.click()
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Optionally close the browser
    driver.quit()