import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Paths to your HH and HV TIFF files
hh_tif_path = "C:\\Users\\ma\\project\\data\\Labdata\\ShahzadpurHH.tif"
hv_tif_path = "C:\\Users\\ma\\project\\data\\Labdata\\ShahzadpurHV.tif"

# Open the TIFF files using rasterio
with rasterio.open(hh_tif_path) as hh_dataset, rasterio.open(hv_tif_path) as hv_dataset:
    hh_data = hh_dataset.read(1)  # Read the first band
    hv_data = hv_dataset.read(1)  # Read the first band
# Calculate the log ratio
combined_data = np.log(hh_data) - np.log(hv_data)

plt.figure(figsize=(8, 8))

plt.imshow(combined_data, cmap='viridis', vmin=0, vmax=1)  # Adjust vmin and vmax as needed
plt.colorbar(label="Log Ratio")
plt.title("HH-HV Composite")
plt.show()