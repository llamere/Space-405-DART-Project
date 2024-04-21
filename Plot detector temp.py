#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from astropy.io import fits
import matplotlib.pyplot as plt
from datetime import datetime

# Directory containing FITS files
directory = r'/Users/lukelamere/fits_files/'

# Initialize lists to store parameter values
detector_temp_list = []
coord_utc_list = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".fits"):
        # Open the FITS file
        fits_file = os.path.join(directory, filename)
        hdul = fits.open(fits_file)

        # Extract data from the header
        header = hdul[0].header

        # Append parameter values to the lists
        detector_temp_list.append(float(header['DETTEMP1']))  # Assuming detector temperature 1 is of interest
        
        # Convert UTC time to datetime object
        utc_time = datetime.strptime(header['COR_UTC'], '%Y-%m-%dT%H:%M:%S')
        coord_utc_list.append(utc_time)

        # Close the FITS file
        hdul.close()

# Plot detector temperature vs time
plt.figure(figsize=(10, 6))
plt.plot(coord_utc_list, detector_temp_list, marker='o', linestyle='-', color='g')
plt.title('Detector Temperature vs Time')
plt.xlabel('Time (UTC)')
plt.ylabel('Detector Temperature (degC)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

