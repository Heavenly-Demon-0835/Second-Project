from flask import Flask, render_template, request, redirect, url_for
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
import time
import logging

app = Flask(__name__)

# Base directory for storing images
BASE_DIR = r"C:\Image Scrapping\Static"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_folder(base_dir, folder_name):
    """
    Creates a folder using 'x' mode behavior. Throws an error if the folder already exists.
    """
    folder_path = os.path.join(base_dir, folder_name)
    
    # Check if folder already exists
    if os.path.exists(folder_path):
        raise FileExistsError(f"Folder '{folder_name}' already exists.")
    
    os.makedirs(folder_path)  # Create the folder if it doesn't exist
    logging.info(f"Created new directory: {folder_path}")
    return folder_path

def download_images(url, folder_name):
    """
    Scrapes images from the given URL and saves them in a specified folder.
    """
    try:
        folder_path = create_folder(BASE_DIR, folder_name)  # Create a new folder
    except FileExistsError as e:
        return str(e)  # Return error message to display on the webpage
    
    # Launch non-headless browser
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(5)
    
    # Scroll down to load images
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)
    
    # Find all images on the page
    images = driver.find_elements(By.TAG_NAME, 'img')
    logging.info(f"Found {len(images)} images on the page.")
    
    for i, image in enumerate(images):
        try:
            src = image.get_attribute('src')
            if src:
                response = requests.get(src, stream=True)
                if response.status_code == 200:
                    file_path = os.path.join(folder_path, f"image_{i + 1}.jpg")
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    logging.info(f"Downloaded: {file_path}")
        except Exception as e:
            logging.error(f"Error downloading image {i + 1}: {e}")
    
    driver.quit()
    return f"Successfully downloaded {len(images)} images to '{folder_path}'"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        folder_name = request.form['folder_name']
        url = request.form['url']
        message = download_images(url, folder_name)
        return render_template('index.html', message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
