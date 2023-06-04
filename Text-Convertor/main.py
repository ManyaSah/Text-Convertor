# import webbrowser
# website_link = input("Enter the link of the website. ")
# url = website_link
# webbrowser.register('chrome',
#                     None,
#                     webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
# webbrowser.get('chrome').open(url)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
import requests
from win10toast import ToastNotifier


def take_screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    print(screenshot)
    return Image.open(BytesIO(screenshot))


# def send_notification(title, message):
#     toaster = ToastNotifier()
#     toaster.show_toast(title, message)


# def process_screenshot(screenshot, instruction):
#     # Process the screenshot and instruction using the desired API
#     # Replace the following code with the actual processing and API call
#     processed_data = f"Processed screenshot using instruction: {instruction}"
#     return processed_data


def main():
    url = input("Enter the website URL: ")
#     frequency = int(input("Enter the frequency in seconds: "))
#     instruction = input("Enter the instruction for processing the screenshot: ")

#     while True:
        screenshot = take_screenshot(url)
#         processed_data = process_screenshot(screenshot, instruction)
#         send_notification("Screenshot Processed", processed_data)
#         time.sleep(frequency)


# if __name__ == "__main__":
    main()
