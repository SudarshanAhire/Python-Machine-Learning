import random 

x = 2
actual_output = 10

print("INPUT VALUE       :", x)
print("EXPECTED OUTPUT   :", actual_output)

weight = random.uniform(0, 1)
learning_rate = 0.1

print("\nINITIAL SETTINGS")
print("----------------")
print("Initial Weight   :", weight)
print("Learning Rate    :", learning_rate)

print("\n===================================================")
print("TRAINING STARTED")
print("===================================================\n")

for step in range(1, 11):
    print(f"\n------------ STEP {step} ------------")

    predicted_output = x * weight 

    print("\nFORWARD PASS")
    print(f"Predicted Output = {x} * {weight} = {predicted_output}")

    error = actual_output - predicted_output

    print("\nERROR CALCULATION")
    print(f"Error = {actual_output} - {predicted_output} = {error}")

    loss = error ** 2

    print("\nLOSS CALCULATION")
    print(f"Loss = Error^2 = {loss}") 

    print("\nWEIGHT UPDATE")
    print(f"Old weight = {weight}")

    weight = weight + (learning_rate * error * x) 

    print(f"New Weight = Old Weight + (Learning Rate * Error * Input)")
    print(f"New Weight = {weight}")


print("\n===================================================")
print("TRAINING COMPLETED")
print("===================================================\n")

final_output = x * weight

print(f"Final Weight      :", weight)
print(f"Final Prediction  :", final_output)
print(f"Expected Output   :", actual_output)