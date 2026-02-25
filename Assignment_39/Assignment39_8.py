import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
)

Border = "-"*40

#################################################################################################
# Step 1 - Load the dataset
#################################################################################################

print(Border)
print("Step 1- Load the Dataset")
print(Border)

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print("Dataset gets loaded succesfully...")


#################################################################################################
# Step 2 - Data Analysis (EDA)
#################################################################################################

print(Border)
print("Step 2 - Data Analysis")
print(Border)

print("Shape of dataset :", df.shape)
print("Column names :", list(df.columns))

print("Missing values (per column)")
print(df.isnull().sum())

print("Class distribution (result count)")
print(df["FinalResult"].value_counts())

print("Statistical Report of dataset")
print(df.describe())

#################################################################################################
# Step 3 - Visualisation of Dataset
#################################################################################################

print(Border)
print("Step 3 - Visualisation of Dataset")
print(Border)

plt.figure(figsize=(8, 5))

plt.hist(df["FinalResult"])

plt.title("Analysis of students Data")
plt.xlabel("Pass OR Fail")
plt.ylabel("Number Of Students")

plt.xticks(range(0, 2, 1))

plt.yticks(range(2, 31, 2))

plt.show()

#################################################################################################
# Step 4 - Split the dataset for training
#################################################################################################

print(Border)
print("Step 4 - Split the dataset for training")
print(Border)

# Test size = 20%
# Train size = 80%

features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

X = df[features]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Data Splitting Activity Done :")

print("X - Independent : ", X.shape)
print("Y - Dependent : ", Y.shape )

print("X_train :", X_train.shape) 
print("X_test :", X_test.shape) 

print("Y_train :", Y_train.shape)
print("Y_test :", Y_test.shape) 


#################################################################################################
# Step 5 - Model selection and training
#################################################################################################

print(Border)
print("Step 5 - Model selection and training")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X_train, Y_train)


print("Model training completed")


#################################################################################################
# Step 6 - Prediction
#################################################################################################

print(Border)
print("Step 6 - Prediction")
print(Border)

Y_pred = model.predict(X_test)

print("Model prediction completed")

print(Y_pred.shape)

print("Expected Answers : ")
print(Y_test)

print("Predicted Answers : ")
print(Y_pred)

#################################################################################################
# Step 7 - Accuracy Calculation
#################################################################################################

print(Border)
print("Step 7 - Accuracy Calculation")
print(Border)

Accuracy = accuracy_score(Y_pred, Y_test)
print("Accuracy of model is :", Accuracy*100)

#################################################################################################
# Step 8 - Confusion matrix generation
#################################################################################################

print(Border)
print("Step 8 - Confusion matrix generation")
print(Border)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion matrix :")
print(cm)


#################################################################################################
# Step 9 - Final Conclusion
#################################################################################################

print(Border)
print("Step 8 - Final Conclusion")
print(Border)







