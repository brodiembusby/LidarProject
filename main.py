import matplotlib.pyplot as plt
import pandas as pd
import math
import csv

zero_reference = 0
z_coordinate = 0
x_offset = 0
begin_calculation = False

def process_data(file_path):
    """
    Reads a .txt file, extracts servo angle and distance readings, and returns them as lists.

    Args:
        file_path (str): The path to the .txt file.

    Returns:
        tuple: Two lists containing the extracted data:
            * servo_angles (list): A list of servo angles (floats).
            * distances (list): A list of distance readings (floats).
    """

    servo_angles = []
    distances = []


    with open(file_path, 'r') as file:
            for line in file:
                values = line.split() 
                if len(values) >= 2:  # Check if there are at least two values
                    servo_angles.append(float(values[0])) 
                    distances.append(float(values[1]))   
                else:
                    print(f"Skipping line due to missing data: {line}") 


    return servo_angles, distances

def calculate_offset(distance, angle, height):
    if angle < 0:
         return -math.sqrt(distance ** 2 - height ** 2)
    
    else: return math.sqrt(distance ** 2 - height ** 2)


# Example usage
file_path = 'data.txt'  # Replace with the path to your file
servo_angles, distances = process_data(file_path)

x = []
y = []
z = []
# This only give three points
# for i in range(len(servo_angles)):
#     if servo_angles[i] == 0:
#         zero_reference = distances[i]
#         z_coordinate += 0.15
#     x_offset = calculate_offset(distances[i], servo_angles[i], zero_reference)
#     x.append(x_offset)
#     y.append(distances[i])
#     z.append(round(z_coordinate, 2))
# this looks better
for i in range(len(servo_angles)):
    if servo_angles:
        zero_reference = distances[i]
        begin_calculation = True
        z_coordinate += 0.15
    
    if begin_calculation:
        x_offset = calculate_offset(distances[i], servo_angles[i], zero_reference)
        x.append(x_offset)
        y.append(distances[i])
        z.append(round(z_coordinate,2))
# Open a new CSV file in write mode
with open("RealData.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Iterate over the arrays simultaneously using zip()
    for x_val, y_val, z_val in zip(x, y, z):
        # Write each set of points on a new line in the CSV file
        writer.writerow([y_val, x_val, z_val])

# Read the CSV file into a DataFrame with custom column names
column_names = ['X', 'Y', 'Z']

data = pd.read_csv('RealData.csv', names=column_names)

# Access the values of X, Y, and Z columns
X = data['X'].values
Y = data['Y'].values
Z = data['Z'].values

# Other cmaps that look good seismic, BrBG and tab20b cmap='tab20b',
fig = plt.figure(num='Lidar Drone Project')
ax = fig.add_subplot(111, projection='3d')
# Add color and actual plotting of data
ax.scatter(X, Y, Z,  c="blue",  marker='.')

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