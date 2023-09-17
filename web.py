import requests
from bs4 import BeautifulSoup
import pdfkit

# Define the URL of the website you want to scrape
url = 'https://www.phoenix.ai/'

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text content from the HTML
    text = soup.get_text()

    # Define the output PDF file name
    pdf_file = 'output.pdf'

    # Specify the path to the wkhtmltopdf executable
    wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Replace with the actual path

    # Configure pdfkit with the path to wkhtmltopdf
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    # Use the configured pdfkit for PDF generation
    pdfkit.from_string(text, pdf_file, configuration=pdfkit_config)

    print(f"PDF generated successfully: {pdf_file}")
else:
    print("Failed to retrieve the web page.")
