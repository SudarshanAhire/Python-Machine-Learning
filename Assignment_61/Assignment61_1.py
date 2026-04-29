from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

X = [
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
]

y = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

model = MLPClassifier(
    hidden_layer_sizes=(5, ),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

model.fit(X_train, Y_train)

new_customer = [[46, 1450, 5, 6, 9]]
new_customer_scaled = scaler.fit_transform(new_customer)

prediction = model.predict(new_customer_scaled)

if prediction  == 1:
    print("Customer Will leave")
else:
    print("Customer will stay")

