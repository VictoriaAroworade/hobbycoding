# ZILLOW WEB SCRAPING + GOOGLE DOC TRANSFER
# AUTHOR: VICTORIA AROWORADE

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_URL = "https://forms.gle/RZ2wyLwM4NUJKpAt7"

# Scrape + Format Zillow Data
response = requests.get(ZILLOW_URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# address list
find_address = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
addresses = [address.getText().strip () for address in find_address]

# price list
find_prices = soup.find_all(name="div", class_="PropertyCardWrapper")
prices = ["".join(char for char in price.text.strip() if char.isdigit()) for price in find_prices]

# link list
find_links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
links = [link.get("href") for link in find_links]



# Create Driver + Complete Online Form

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM_URL)

# input responses

# location
for item1, item2, item3 in zip(addresses, prices, links):
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div').click()
    location = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    location.send_keys(f"{item1}")

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div').click()
    cost = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cost.send_keys(f"${item2}")

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div').click()
    url = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url.send_keys(f"{item3}")

    # submit
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    driver.get(GOOGLE_FORM_URL)

driver.quit()




