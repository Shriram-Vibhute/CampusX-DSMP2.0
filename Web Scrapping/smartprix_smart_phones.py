from selenium import webdriver
from selenium.webdriver.chrome.service import Service # To set webdriver
from selenium.webdriver.chrome.options import Options # For setting the behavour of browsers
from selenium.webdriver.common.by import By # setting the format of finding the element
from selenium.webdriver.common.keys import Keys # Automating keyboard keys
import time # For introducing delay for loading the entire page before triggring next automation code

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
driver = webdriver.Chrome(service = s, options = chrome_options)
driver.get("https://www.smartprix.com/mobiles")
time.sleep(5)

# Clicking on filters
driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(5)
driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
print("Filters Enabled")

height = driver.execute_script('return document.body.scrollHeight') # Getting the height of entire height until 2nd load
print(height)
time.sleep(5)

old_height, new_height = height, 0
for i in range(10):
    driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
    time.sleep(5)  # Wait for new html = driver.page_source
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height, new_height)
    if new_height == old_height:
        break
    old_height = new_height

# Saving the entire content into html file
html = driver.page_source
with open(file = "smartphones.html", mode = 'w', encoding = 'utf-8') as f:
    f.write(html)

# Exit Driver
driver.quit()