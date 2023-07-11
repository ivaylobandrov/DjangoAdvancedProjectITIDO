from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os


class Command(BaseCommand):
    """Django custom command which downloads csv file from a specific url
    and saves it into a given path"""

    help = "Download CSV file using Selenium"

    def handle(self, *args, **options):
        # Specify the path to the Chrome WebDriver
        webdriver_path = os.environ.get("WEBDRIVER_PATH", "/opt/homebrew/bin/chromedriver")

        # Specify the download directory for the CSV file
        download_path = os.environ.get("DOWNLOAD_PATH", "/app/portal/csv_files")

        # Create the download directory if it doesn't exist
        os.makedirs(download_path, exist_ok=True)

        # Configure the Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "download.default_filename": "data.csv"
        })

        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(service=Service(executable_path=webdriver_path), options=chrome_options)

        try:
            # Open the website URL
            driver.get("https://ibex.bg/%D0%B4%D0%B0%D0%BD%D0%BD%D0%B8-%D0%B7%D0%B0-%D0%BF%D0%B0%D0%B7%D0%B0%D1%80%D0%B0/%D0%BF%D0%B0%D0%B7%D0%B0%D1%80%D0%B5%D0%BD-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%B4%D0%B5%D0%BD-%D0%BD%D0%B0%D0%BF%D1%80%D0%B5%D0%B4/%D0%BF%D0%B0%D0%B7%D0%B0%D1%80%D0%B5%D0%BD-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82-%D0%B4%D0%B5%D0%BD-%D0%BD%D0%B0%D0%BF%D1%80%D0%B5%D0%B4-2/")  # Replace with the actual website URL

            # Locate the button using the onclick attribute
            button = driver.find_element(By.XPATH, "//button[@onclick='csvFunc()']")

            # Click the button using JavaScript execution
            driver.execute_script("arguments[0].click();", button)

            # Wait for the file to download
            time.sleep(5)  # Adjust the waiting time if necessary

            # Get the latest downloaded file in the directory
            files = os.listdir(download_path)
            latest_file = files[-1]
            original_file_path = os.path.join(download_path, latest_file)

            # Rename the file to 'data.csv'
            new_file_path = os.path.join(download_path, "data.csv")
            os.rename(original_file_path, new_file_path)

        finally:
            # Close the driver to release resources
            driver.quit()

        self.stdout.write(self.style.SUCCESS("CSV file downloaded successfully."))
