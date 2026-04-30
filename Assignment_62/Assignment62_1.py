import numpy as np

#-------------------------------------------------------------
# Step 1 - 5 x 5 Image
#-------------------------------------------------------------

Image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

print("\nOriginal 5x5 Image")
print(Image)

#-------------------------------------------------------------
# Step 2 -  3x3 kernel for Horizontal Edge detection 
#-------------------------------------------------------------

kernel = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

print("\n3x3 Kernel")
print(kernel)

#-------------------------------------------------------------
# Step 3 - Convolution Operation 
# Output Size = (5-3+1) x (5-3+1)
#-------------------------------------------------------------

feature_map = np.zeros((3, 3))

for i in range(3):
    for j in range(3):

        # Extract 3x3 region 
        region = Image[i:i+3, j:j+3]

        print("------------------------------------")
        print("\nRegion :")
        print(region)

        matrix = region * kernel
        print("\nkernel * region :\n",matrix)

        # Multiply and Sum 
        result = np.sum(region * kernel)
        print("\nOutput : ", result)

        # Store result 
        feature_map[i][j] = result 
        print("\nFeature Map :")
        print(feature_map)

#-------------------------------------------------------------
# Step 4 : Show Feature map 
#-------------------------------------------------------------

print("\nFeature Map (Detected Edge)")
print(feature_map)






