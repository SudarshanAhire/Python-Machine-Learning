import numpy as np

def main():
    X = np.array([5, 7, 9, 11, 13])

    # calculating the mean of dataset
    mean_X = sum(X) / len(X)
    print("Mean of X is :", mean_X)

    # calculating the variance of dataset
    deviation_of_EachVal = [float(val-mean_X) for val in X]
    print("Deviation list of each val :", deviation_of_EachVal)
    
    # calculating standerd deviation
    square_list = [val*val for val in deviation_of_EachVal]
    sum_of_squre_list_val = sum(square_list)

    variance = sum_of_squre_list_val / len(square_list)

    print("variance of the dataset is :", variance)


if __name__ == "__main__":
    main()