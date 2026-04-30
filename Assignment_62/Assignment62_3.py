import numpy as np

def Flatten(data):
    
    print("Input to flatten :\n", data)
    flat = data.flatten()

    print("\nFlattened ouput :\n", flat)

    return flat

def fully_connected_layer(flat_data):

    print("\n-----------Fully Connected Layer----------")

    weights = np.array([1, 1, 1, 1], dtype=float)
    bias = 0.0

    print("\nFlatten Input :")
    print(flat_data)

    print("\nweights :", weights)

    print("Bias :", bias)

    multiplication = flat_data * weights 
    result = np.sum(multiplication) + bias 

    print("\nInput * weights :")
    print(multiplication)

    print("\nSum =", np.sum(multiplication))
    print("\nFinal output after adding bias =", result)

    return result

def sigmoid(data):
    return 1 / (1 + np.exp(-data))

def main():

    matrix = np.array([
        [6, 4],
        [8, 6]
    ])

    flatten_data = Flatten(matrix)

    FC_score = fully_connected_layer(flatten_data)
    print("\nScore of fully connected layer :", FC_score)

    final_output = sigmoid(FC_score)
    print("\nFinal Output :", final_output)

    print("\nRole of flatten layer : The flatten layer convert the matrix in 1D vector to \npass the input to dense layer.")

if __name__ == "__main__":
    main()