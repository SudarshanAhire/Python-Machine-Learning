import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

inputs = np.array([2, 3])       # x1 = 2, x2 = 3

weights = np.array([0.4, 0.6])  # w1 = 0.4, w2 = 0.6

bias = 0.5                      # b = 0.5

weighted_sum = sum(w * x for w, x in zip(inputs, weights)) + bias

print(weighted_sum)

z_hat = sigmoid(weighted_sum)

print("Output after sigmoid function :", z_hat)

print(f"The output of the sigmoid function is {z_hat} which is closer to 1.")






