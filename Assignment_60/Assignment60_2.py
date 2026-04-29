import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def ReLU(z):
    return np.maximum(0, z)

def Tanh(z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

def plot_sigmoid():

    # Generate input range
    z_values = np.linspace(-10, 10, 200)

    # Apply sigmoid on range
    sigmoid_values = 1 / (1 + np.exp(-z_values))

    # Plot graph
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, sigmoid_values, label="Sigmoid Function", linewidth=2, color="blue")

    # Reference lines
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axhline(y=1, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")

    # Labels and title
    plt.title("Sigmoid Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output (Probability)", fontsize=14)

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()


def plot_relu():

    # Generate range of values for z
    z_values = np.linspace(-10, 10, 200)

    # Apply ReLU on all values
    relu_values = np.maximum(0, z_values)

    # Plot graph
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, relu_values, label="ReLU Function", linewidth=2, color="green")

    # Axes lines
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")

    # Labels and title
    plt.title("ReLU Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # Show graph
    plt.show()

def plot_Tanh():

    # Generate input range
    z_values = np.linspace(-10, 10, 200)

    # Apply Tanh on range
    tanh_values = (np.exp(z_values) - np.exp(-z_values)) / (np.exp(z_values) + np.exp(-z_values))

    # Plot graph
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, tanh_values, label="Tanh Function", linewidth=2, color="orange")

    # Reference lines
    plt.axhline(y=-1, color="black", linewidth=0.5)
    plt.axhline(y=1, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")

    # Labels and title
    plt.title("Tanh Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()

def main():
    
    inputs = np.array([2, 8, 5, 3])

    weiights = np.array([0.3, 0.8, 0.6, 0.1])

    bias = 1.0

    plot_sigmoid()
    print("\n The Sigmoid function add non-linearity to the model and maps any input to a value between 0 and 1, making it ideal for binary classification problems.")

    plot_relu()
    print("\n The ReLU function introduces non-linearity and helps mitigate the vanishing gradient problem.")

    plot_Tanh()
    print("\n The Tanh function maps inputs to a value between -1 and 1, providing zero-centered output.")

if __name__ == "__main__":
    main()