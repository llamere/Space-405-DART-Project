import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Step 1: Read FITS file and create masked array
# Define the directory path where the FITS file is located
directory = r'C:\Users\Nperr\Documents\Climate 405\nbody-python\fits_files\\'

# Concatenate the directory path with the file name
fits_file = directory + 'dart_0401929788_46871_02_iof.fits'  # Include the file extension

# Read the data from the FITS file
with fits.open(fits_file) as hdul:  # Use the fits_file variable
    data = hdul[0].data  # Assuming the data is in the primary HDU

# Define condition for invalid values (e.g., values below a certain threshold)
threshold = 0  # Define your threshold here
mask = np.ma.masked_where(data < threshold, data)

# Step 2: Visualize data with pcolormesh
plt.figure(figsize=(8, 6))
plt.pcolormesh(mask, cmap='viridis', norm=LogNorm())  # You can choose any colormap
plt.colorbar(label='Intensity')
plt.title('Pseudocolor plot of FITS data with invalid values masked')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
