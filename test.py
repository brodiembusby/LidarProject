# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D

# # Convert the strings to lists of floats
# X = "32 20 67 1 98 34 57 65 24 82 47 55 8 51 13 14 18 30 37 39 10 33 21 26 38 81 83 60 95 22 17 5 72 46 99 52 12 25 96 29 70 85 43 69 19 78 97 31 89 53 2 91 48 71 61 15 36 84 94 50 11 80 6 7 49 74 9 88 40 79 27 68 73 64 63 59 86 23 35 58 45 28 100 42 93 87 16 90 41 66 54 92 77 4 62 76 75 56 3 44"
# Y = "96 75 24 9 83 49 27 77 3 23 17 31 40 13 7 52 51 21 98 47 64 79 78 91 44 16 15 100 84 99 63 68 70 30 54 76 97 73 33 5 88 8 71 66 62 25 60 42 72 45 18 11 28 59 89 65 10 55 69 81 12 26 20 95 87 41 74 50 93 22 43 90 14 34 82 35 56 38 80 32 1 57 6 36 37 61 29 58 2 48 4 46 67 53 92 86 94 19 39 85"
# Z = "55 31 11 45 83 36 86 49 15 57 42 46 8 94 88 47 54 81 98 41 32 35 56 85 9 89 37 60 23 62 67 100 78 76 73 80 10 20 68 34 77 93 1 63 53 12 22 99 91 40 84 24 33 3 43 19 92 97 6 82 64 25 26 79 95 4 44 58 5 21 70 29 65 87 96 90 51 14 18 2 72 28 71 39 52 7 27 59 50 61 48 30 66 69 17 13 74 16 75 38"

# X = [float(x) for x in X.split()]
# Y = [float(x) for x in Y.split()]
# Z = [float(x) for x in Z.split()]
# # I like this 


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(X, Y, Z, c=Z, cmap='viridis')  # Default scatter plot
# ax.view_init(elev=30, azim=45)  # Adjust elevation and azimuthal angle
# plt.colorbar(ax.scatter(X, Y, Z, c=Z, cmap='viridis'))  # Add colorbar for reference
# plt.show()

