import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument(
    "--headless"
)  # Run in headless mode if you don't need a browser window
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": "/Users/ivaylobandrov/Desktop/AdvanceDjangoProjectITIDO/app/portal/csv_files",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    },
)

driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website
driver.get(
    "https://ibex.bg/%D0%B4%D0%B0%D0%BD%D0%BD%D0%B8-%D0%B7%D0%B0-%D0%BF%D0%B0%D0%B7%D0%B0%D1%80%D0%B0/%D0%BF%D0%B0%D0%B7%D0%B0%D1%80%D0%B5%D0%BD-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%B4%D0%B5%D0%BD-%D0%BD%D0%B0%D0%BF%D1%80%D0%B5%D0%B4/%D0%BF%D0%B0%D0%B7%D0%B0%D1%80%D0%B5%D0%BD-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%B4%D0%B5%D0%BD-%D0%BD%D0%B0%D0%BF%D1%80%D0%B5%D0%B4-2/"
)

# Find and click the button that triggers the CSV download
csv_button = driver.find_element(By.XPATH, "//button[contains(text(), 'CSV')]")
csv_button.click()

# Wait for the file to download (you can adjust the wait time as needed)
time.sleep(15)

# Close the browser
driver.quit()
