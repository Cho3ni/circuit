
"""
Name:  Tenzin Choeni
Email: tenzin.choeni60@myhunter.cuny.edu
Date:  September 2025
Takes elevation data of NYC and displays using the default color map
"""

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt("elevationsNYC.txt")

intensity = float(input("What intensity for the topo lines: "))
output_filename = input("What is the output file: ")

mapShape = elevations.shape + (3,)
topoMap = np.zeros(mapShape)

for row in range(elevations.shape[0]):
    for col in range(elevations.shape[1]):
        elev = elevations[row, col]
        if elev <= 0:
            topoMap[row, col] = [0.0, 0.0, 1.0]  # Blue
        elif elev % 10 == 0:
            topoMap[row, col] = [intensity, intensity, intensity]  # Gray topo line
        else:
            topoMap[row, col] = [1.0, 1.0, 1.0]  # White

plt.imsave(output_filename, topoMap)

print("Thank you for using my program!")
print(f"Your map is stored {output_filename}.")
