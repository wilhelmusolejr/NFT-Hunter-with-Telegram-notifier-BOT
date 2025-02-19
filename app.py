from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from telegram_sender import notify_user, send_message
from dotenv import load_dotenv

import time
import csv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
target_percentage = os.getenv('TARGET_PERCENTAGE')
print(f'Target Percentage: {target_percentage}')
# -------------

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# Define the CSV file path
csv_file = "nft.csv"

# Read existing data to check for duplicates
existing_ids = set()

try:
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_ids.add(row["id"])
except FileNotFoundError:
    pass  # If the file doesn't exist, it will be created when writing

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
send_message("---------------")

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Required for headless mode on Windows
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes in Docker/Linux

# Set path to ChromeDriver
chrome_driver_path = "chromedriver.exe"  # Change this to your actual path

# Set up the service
service = Service(chrome_driver_path)

# Launch browser with options
driver = webdriver.Chrome(service=service, options=chrome_options)

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# Open a website
driver.get(os.getenv('FLW_URL'))

# Wait for the page to load
time.sleep(5)

# Find the parent UL that contains all NFT cards
parent_ul = driver.find_element(By.CSS_SELECTOR, ".w-full.h-full.grid.pb-4.gap-4")

# Scroll dynamically to load more NFTs
last_count = 0

while True:
    # Get all LI elements inside the parent UL
    nft_cards = parent_ul.find_elements(By.XPATH, "./div")  
    new_count = len(nft_cards)

    if new_count == last_count:  # Stop if no new NFTs load
        break
    
    last_count = new_count
    driver.execute_script("arguments[0].scrollIntoView();", nft_cards[-1])  # Scroll to last card
    time.sleep(10)  # Wait for new items to load
    print("scrolling down...")

print(f"Total NFTs loaded: {len(nft_cards)}")

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# Extract data from each NFT card
for nft in nft_cards:
    try:
        # Check if there's a pending offer
        try:
            offer_element = nft.find_element(By.CSS_SELECTOR, ".nftCard > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) .nft-price")  # Change selector
            offer_text = offer_element.text

            nft_price = nft.find_element(By.CSS_SELECTOR, ".nftCard .nft-price")
            nft_price_text = nft_price.text

            # Convert extracted text to float (remove commas)
            nft_price_value = int(float(nft_price_text.replace(",", "")))
            offer_price_value = int(float(offer_text.replace(",", "")))

            # Calculate percentage
            percentage_decrease = int(((nft_price_value - offer_price_value) / nft_price_value) * 100)

            # Only push to NFT_BUY if percentage is 50% or below
            if percentage_decrease <= target_percentage:
                link = nft.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                id = link.split("/")[-1]

                new_data = {
                    "id": id,  
                    "percentage": percentage_decrease,  
                    "nft_price": nft_price_value,  
                    "offer_price": offer_price_value
                }

                # Append data if ID is not in the file
                if new_data["id"] not in existing_ids:
                    file_exists = True  # Assume the file exists unless proven otherwise

                    try:
                        with open(csv_file, mode="r", encoding="utf-8") as file:
                            file_exists = bool(file.read().strip())  # Check if file has content
                    except FileNotFoundError:
                        file_exists = False  # File doesn't exist

                    # Open in append mode and add header if necessary
                    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
                        fieldnames = ["id", "percentage", "nft_price", "offer_price"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)

                        if not file_exists:
                            writer.writeheader()  # Write header only if the file is empty

                        writer.writerow(new_data)  # Append new data

                    print("New data added to nft.csv.")
                    notify_user(new_data)
                else:
                    print("ID already exists. No data added.")

        except:
            continue  # Skip NFTs without pending offers

    except Exception as e:
        print(f"Error processing NFT: {e}")

    time.sleep(1)


send_message(f"Total NFTs loaded: {len(nft_cards)}")

# Close browser
driver.quit()
