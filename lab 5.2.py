'normalize image'
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
# Normalize the data to a common range for visualization
hh_normalized = (hh_data - np.min(hh_data)) / (np.max(hh_data) - np.min(hh_data))
hv_normalized = (hv_data - np.min(hv_data)) / (np.max(hv_data) - np.min(hv_data))

# Create the color composite
rgb_image = np.zeros((hh_data.shape[0], hv_data.shape[1], 3), dtype=np.float32)
rgb_image[:, :, 0] = hh_normalized  # Red channel for HH
rgb_image[:, :, 1] = hv_normalized  # Green channel for HV

# Clip values to ensure they are within the valid range [0, 1]
rgb_image = np.clip(rgb_image, 0, 1)
plt.figure(figsize=(8, 8))
plt.imshow(rgb_image)
plt.title("HH-HV Color Composite")
plt.show()
# Choose a colormap that highlights the HV data
colormap = plt.get_cmap("viridis")