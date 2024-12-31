# Image Web Scraper from Google

## Overview
Image Web Scraper is a Python-based web application designed to scrape images from Google using Flask as the backend framework and Beautiful Soup for web scraping. This project allows users to search for a specific term and download relevant images directly from the web.

## Features
- User-friendly web interface for inputting search terms.
- Automatically scrapes images related to the provided search term.
- Allows users to download the scraped images.
- Handles requests and web scraping efficiently using Flask and Beautiful Soup.

## Technologies Used
- **Flask**: Backend web framework to serve the application.
- **Beautiful Soup**: Python library used for parsing and scraping HTML content.
- **HTML/CSS**: For creating the frontend user interface.

## Prerequisites
Before running the project, ensure you have the following installed on your system:
- Python 3.7 or higher
- Pip (Python package manager)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ssantrupth/Image-Web-Scraping.git
   cd image-web-scraping
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:3000
   ```

3. Enter a search term in the input field and hit "Search." The application will scrape images from Google and display them.

4. Optionally, download the images displayed.

## File Structure
```
Image-Web-Scrapeing/
|-- app.py                 # Main Flask application
|-- scrapperImage/
|   |-- ScrapperImage.py   # Contains the logic for web scraping
|-- businesslayer/
|   |-- BusinessLayerUtil.py  # Utility functions for processing scraped data
|-- templates/
|   |-- index.html         # Frontend template for the application
|   |-- showImage.html     # Shows the image
|-- static/
|   |-- css/               # Stylesheets
|-- requirements.txt       # List of project dependencies
|-- README.md              # Project documentation
```

## Dependencies
- Flask
- Beautiful Soup 4
- Requests

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Important Notes
- **Google Search Scraping Limitations**: Scraping Google is against their terms of service. Use this project for educational purposes only and avoid excessive requests.
- If SSL certificate verification issues occur, ensure your Python installation has updated certificates. See the troubleshooting section below.

## Troubleshooting
1. **SSL Certificate Error**:
   Run the following command to fix certificate issues (macOS-specific):
   ```bash
   /Applications/Python\ 3.x/Install\ Certificates.command
   ```

2. **Dependencies Not Installing**:
   Ensure you're using a virtual environment and Python 3.7 or higher.

3. **Scraper Failing to Fetch Images**:
   - Check your internet connection.
   - Google may block requests due to rate limiting; consider adding delays between requests.

## Acknowledgments
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/)

---

**Disclaimer**: This project is for educational purposes only. Use responsibly and adhere to legal and ethical standards.
