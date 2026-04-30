import numpy as np

def relu(z):
    return np.maximum(0, z)

def relu_matrix(feature_map):
    
    rows, cols = feature_map.shape 
    
    output = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            result = relu(feature_map[i][j])
            output[i][j] = result

    return output

def pooling(relu_matrix):

    rows, cols = relu_matrix.shape
    output_rows = rows // 2
    output_cols = cols // 2

    output = np.zeros((output_rows, output_cols))

    r = 0
    for i in range(0, rows, 2):
        c = 0
        for j in range(0, cols, 2):

            block = relu_matrix[i:i+2, j:j+2]

            if block.shape != (2, 2):
                continue

            max_value = np.max(block)
            output[r][c] = max_value

            c = c + 1
        r = r + 1

    return output

def main():

    feature_map = np.array([
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ])

    print("\nFeature Map :\n", feature_map)

    relu = relu_matrix(feature_map)
    print("\nFeature Map after relu activation :\n", relu)

    max_pool = pooling(relu)
    print("\nRelu Matrx after max pooling :\n", max_pool)

    print("The Max Pooling reduces size beacuse of optimization of image size.")

            
if __name__ == "__main__":
    main()
