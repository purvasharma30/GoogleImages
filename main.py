import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome options and WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--incognito')  # Run Chrome in incognito mode
driver = webdriver.Chrome(options=chrome_options)

# Open the URL
URL = 'https://www.google.com/search?q=nasi+kandar&sca_esv=573788213&tbm=isch'
driver.get(URL)

# Create a directory for saving images
os.makedirs("NasiKandarImages", exist_ok=True)
image_dir = "NasiKandarImages"

# Counter to keep track of downloaded images
image_counter = 0

# Function to scroll and download images
def scroll_and_download_images(scrolls):
    global image_counter
    for scroll in range(scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # Collect image elements
        image_elements = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
        
        for i, img in enumerate(image_elements):
            image_url = img.get_attribute("src")
            if image_url:
                try:
                    image_data = requests.get(image_url, stream=True).content
                    with open(f"{image_dir}/nasi_kandar_{image_counter}.jpg", "wb") as image_file:
                        image_file.write(image_data)
                    print(f"Image {image_counter} downloaded")
                    image_counter += 1

                except Exception as e:
                    print(f"Error downloading image {i}: {e}")

# Specify the number of scrolls
scrolls = 10

scroll_and_download_images(scrolls)

# Close the browser
driver.quit()
