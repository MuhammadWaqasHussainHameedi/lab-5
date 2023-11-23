'normalized seismic'
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

# Normalize the intensity values of HH and HV data to the [0, 1] range
hh_normalized = (hh_data - np.min(hh_data)) / (np.max(hh_data) - np.min(hh_data))
hv_normalized = (hv_data - np.min(hv_data)) / (np.max(hv_data) - np.min(hv_data))

# Calculate the difference between HH and HV
difference = hh_normalized - hv_normalized

# Choose a colormap that emphasizes contrasts
colormap = plt.get_cmap("seismic")  # Diverging colormap

# Apply the colormap to the difference image
difference_colormap = (colormap(difference)[:, :, :3] * 255).astype(np.uint8)

# Display the difference composite image
plt.figure(figsize=(8, 8))
plt.imshow(difference_colormap)
plt.title("HH-HV Difference Composite")
plt.axis('off')  # Turn off axes

plt.show()
