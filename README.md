# Web Scraping and PDF Conversion with Python

## Description:
This Python script allows you to scrape text content from a specified website and convert it into a PDF file. It utilizes popular libraries such as requests, BeautifulSoup, and pdfkit to accomplish this task.

## How it works:

The script starts by defining the URL of the website you want to scrape. In this example, we've used 'https://www.phoenix.ai/' as the target website.
It sends an HTTP GET request to the specified URL to retrieve the web page's content.
Upon receiving a successful response (HTTP status code 200), the HTML content is parsed using BeautifulSoup to extract the text content.
The extracted text content is then converted into a PDF file.
To convert the text to a PDF, we specify the path to the wkhtmltopdf executable, which is an external tool used for HTML to PDF conversion. The path is configured in the pdfkit_config variable.
Finally, the script uses the configured pdfkit to generate the PDF file, and the user is provided with a message indicating whether the PDF was generated successfully or if there was a failure.
## Usage:

You can customize the script by changing the target URL and the output PDF file name according to your needs.
Make sure to replace the wkhtmltopdf_path variable with the actual path to the wkhtmltopdf executable on your system.

## Requirements:

Python
requests library
BeautifulSoup library
pdfkit library
wkhtmltopdf tool (external dependency)
## Note:
Before running the script, ensure that you have wkhtmltopdf installed on your system and that the path to the wkhtmltopdf executable is correctly specified in the script.

Feel free to use and modify this script for your web scraping and PDF conversion needs. Happy coding!
