# Image Scraper Web Application

## Project Overview

The **Image Scraper Web Application** is a Python-based web application that allows users to scrape images from any given URL and store them in a user-specified folder. The application uses Selenium for web scraping, Flask for the web interface, and dynamically creates directories for each scraping session to ensure that images from different websites are stored separately.

## Features

1. **User-Friendly Interface**:

   - The application provides a simple HTML form for users to enter the folder name and URL.
   - Displays success or error messages based on the scraping outcome.

2. **Dynamic Folder Creation**:

   - A new folder is created for each scraping session based on the user-provided folder name.
   - If a folder with the same name already exists, an error message is shown to the user, prompting them to choose a different folder name.

3. **Non-Headless Browsing**:

   - The browser opens in a non-headless mode, allowing users to see the scraping process in real-time.

4. **Image Downloading**:

   - The script automatically scrolls through the webpage to load more images.
   - Identifies all image tags on the page, extracts the image URLs, and downloads the images to the specified folder.
   - **Note**: The program downloads every image it finds on the webpage, including advertisements, icons, and other non-relevant images. It does not filter for clean images.

5. **Duplicate Images**:

   - The program may download duplicate images if they are found multiple times on the webpage.

6. **Logging**:

   - Logs are displayed in the terminal to indicate the progress of scraping and downloading.

## How It Works

1. **Folder Creation**:

   - The application attempts to create a folder using the name provided by the user.
   - If a folder with the same name already exists, an error message is displayed.

2. **Image Scraping**:

   - The browser opens and navigates to the provided URL.
   - The page is scrolled multiple times to load all images.
   - All image tags (`<img>`) are identified, and their `src` attributes are extracted.
   - The images are downloaded and saved in the specified folder.

3. **File Storage**:

   - All images are saved in the following path: `C:\Image Scrapping\Static\<Folder_Name>`.

## Requirements

- Python 3.x
- Flask
- Selenium
- ChromeDriver (Ensure the version matches your Chrome browser)
- Google Chrome browser

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd image-scraper-webapp
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up ChromeDriver:

   - [Download ChromeDriver](https://sites.google.com/chromium.org/driver/) matching your Chrome browser version.
   - Place the ChromeDriver executable in a directory included in your system's PATH.

4. Create the base directory for storing images:

   ```bash
   mkdir "C:\Image Scrapping\Static"
   ```

5. Run the Flask application:

   ```bash
   python Image_Scraper_Webpage.py
   ```

6. Open your browser and go to `http://127.0.0.1:5000` to use the application.

## Usage

1. Enter the desired folder name.
2. Enter the URL of the webpage containing the images.
3. Click the "Scrape Images" button.
4. View the downloaded images in the specified folder under `C:\Image Scrapping\Static\`.

## Example

1. **Folder Name**: Ikea
2. **URL**: `https://www.ikea.com/in/en/cat/curtains-blinds-tl002/`

Upon successful scraping, the images will be saved in:

```bash
C:\Image Scrapping\Static\Ikea
```

## Error Handling

- If a folder with the same name already exists, an error message will be displayed:
  **"Folder '\<folder\_name>' already exists. Choose a different name."**

## File Structure

```bash
image-scraper-webapp/
|-- Image_Scraper_Webpage.py  # Main Python script for scraping
|-- templates/
|   `-- index.html            # HTML form for user input
|-- static/                   # Directory where images are saved
|-- requirements.txt          # Python dependencies
|-- README.md                 # Project documentation
```

## Technologies Used

- **Python**: Backend logic and web scraping.
- **Flask**: Web framework for building the web interface.
- **Selenium**: Web scraping and browser automation.
- **HTML/CSS**: Frontend interface.
- **Google Chrome**: Browser for non-headless scraping.

## Future Enhancements

- Add support for parallel scraping of multiple URLs.
- Implement a progress bar on the web interface.
- Allow users to set custom scrolling limits.
- Add image format validation (only download specific formats like JPG, PNG, etc.).
- **Filter Clean Images**: Implement a filtering mechanism to download only relevant images.
- **Remove Duplicates**: Add logic to detect and prevent downloading duplicate images.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Author

[Jay]\
Feel free to connect on [https://www.linkedin.com/in/jay-dave-08mar05/ or](https://www.linkedin.com/in/jay-dave-08mar05/ or) drop a mail at [jaydave.0835\@gmail.com].


