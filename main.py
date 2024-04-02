import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame with custom column names
column_names = ['X', 'Y', 'Z']
data = pd.read_csv('TestData.csv', names=column_names)

# Access the values of X, Y, and Z columns
X = data['X'].values
Y = data['Y'].values
Z = data['Z'].values

# Other cmaps that look good seismic, BrBG and tab20b
fig = plt.figure(num='Lidar Drone Project')
ax = fig.add_subplot(111, projection='3d')
# Add color and actual plotting of data
ax.scatter(X, Y, Z,  c=Z, cmap='tab20b', marker='.')

# Set titles and labels
ax.set_title('3D Point Cloud Plot using Lidar Data')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_box_aspect((1, 1, 1))  # Set equal aspect ratio for all axes
x_min, x_max = min(X), max(X)
y_min, y_max = min(Y), max(Y)
z_min, z_max = min(Z), max(Z)
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_zlim(z_min, z_max)
plt.show()
