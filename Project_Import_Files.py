import requests
from bs4 import BeautifulSoup
from astropy.io import fits
from PIL import Image
import xml.etree.ElementTree as ET
from io import BytesIO
import os

base_url = 'https://pds-smallbodies.astro.umd.edu/holdings/pds4-dart:data_dracocal-v3.0/final/2022/269/'

# Initialize counters for file types
fits_count = 0
png_count = 0
xml_count = 0

# Define directories to save files
fits_dir = 'fits_files/'
png_dir = 'png_files/'
xml_dir = 'xml_files/'

# Create directories if they don't exist
os.makedirs(fits_dir, exist_ok=True)
os.makedirs(png_dir, exist_ok=True)
os.makedirs(xml_dir, exist_ok=True)

# Function to download and process FITS files
def process_fits(url):
    global fits_count
    full_url = base_url + url  # Construct the full URL
    response = requests.get(full_url)
    if response.status_code == 200:
        filename = os.path.basename(url)
        with fits.open(BytesIO(response.content)) as hdul:
            hdul.writeto(os.path.join(fits_dir, filename), overwrite=True)
            fits_count += 1
            print("Imported FITS file:", full_url)
    else:
        print(f"Failed to download FITS file from {full_url}")

# Function to download and process PNG files
def process_png(url):
    global png_count
    full_url = base_url + url  # Construct the full URL
    response = requests.get(full_url)
    if response.status_code == 200:
        filename = os.path.basename(url)
        with open(os.path.join(png_dir, filename), 'wb') as file:
            file.write(response.content)
            png_count += 1
            print("Imported PNG file:", full_url)
    else:
        print(f"Failed to download PNG file from {full_url}")

# Function to download and process XML files
def process_xml(url):
    global xml_count
    full_url = base_url + url  # Construct the full URL
    response = requests.get(full_url)
    if response.status_code == 200:
        filename = os.path.basename(url)
        with open(os.path.join(xml_dir, filename), 'wb') as file:
            file.write(response.content)
            xml_count += 1
            print("Imported XML file:", full_url)
    else:
        print(f"Failed to download XML file from {full_url}")

# URL of the webpage
url = 'https://pds-smallbodies.astro.umd.edu/holdings/pds4-dart:data_dracocal-v3.0/final/2022/269/'  

# Fetch the webpage content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all links on the page
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href.endswith('.fits'):
            process_fits(href)
        elif href.endswith('.png'):
            process_png(href)
        elif href.endswith('.xml'):
            process_xml(href)
else:
    print("Failed to fetch the webpage")

# Print the counts for each file type
print("Number of FITS files retrieved:", fits_count)
print("Number of PNG files retrieved:", png_count)
print("Number of XML files retrieved:", xml_count)
