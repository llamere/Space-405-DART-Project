import requests
from bs4 import BeautifulSoup
from astropy.io import fits
from PIL import Image
import xml.etree.ElementTree as ET
from io import BytesIO
import os

base_url = 'https://pds-smallbodies.astro.umd.edu/holdings/pds4-dart:data_dracocal-v3.0/final/2022/269/'

# Initialize counters
total_files = 0
fits_count = 0
png_count = 0
xml_count = 0

# Function to download and process FITS files
def process_fits(url):
    global total_files, fits_count
    full_url = base_url + url  # Construct the full URL
    response = requests.get(full_url)
    if response.status_code == 200:
        with fits.open(BytesIO(response.content)) as hdul:
            fits_count += 1
            total_files += 1
    else:
        print(f"Failed to download FITS file from {full_url}")

# Function to download and process PNG files
def process_png(url):
    global total_files, png_count
    full_url = base_url + url  # Construct the full URL
    response = requests.get(full_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        png_count += 1
        total_files += 1
    else:
        print(f"Failed to download PNG file from {full_url}")

# Function to download and process XML files
def process_xml(url):
    global total_files, xml_count
    full_url = base_url + url  # Construct the full URL
    response = requests.get(full_url)
    if response.status_code == 200:
        xml_root = ET.fromstring(response.content)
        xml_count += 1
        total_files += 1
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

# Print the totals
print("Total number of files imported:", total_files)
print("Total number of FITS files imported:", fits_count)
print("Total number of PNG files imported:", png_count)
print("Total number of XML files imported:", xml_count)
