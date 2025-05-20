from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up driver
service = Service("C:/Users/MITS/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Open target page
driver.get("https://www.eurasiantimes.com/pakistans-jf-17-shoots-down-six-rafale-fighters-during-turkish/")
time.sleep(2)

# File to store links
path = 'D:/web scrapping/project_1/links.txt'
links = []

# Get text from target element
results = driver.find_elements(By.XPATH, '//*[@id="post-157757"]/div[3]/p[2]')
for result in results:
    text = result.text
    print(text)
    links.append(text)

# Navigate to another page
driver.find_element(By.XPATH, '//*[@id="menu-header-menu-3"]/li[2]/a').click()
time.sleep(2)

# Get all <a> tag href links
anchors = driver.find_elements(By.TAG_NAME, "a")
for a in anchors:
    href = a.get_attribute("href")
    if href:
        links.append(href)

# Write all links and text to file
with open(path, 'w', encoding='utf-8') as f:
    for link in links:
        f.write(link + "\n")

# Save screenshot
driver.save_screenshot("D:/web scrapping/project_1/img.png")

# Quit browser
driver.quit()
