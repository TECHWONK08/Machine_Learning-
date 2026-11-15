from sklearn.linear_model import LinearRegression

# House sizes in square feet
X = [
    [500],
    [800],
    [1000],
    [1200],
    [1500]
]

# House prices in lakh rupees
y = [20, 32, 40, 48, 60]

# Create the machine learning model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict the price of a new house
new_house = [[1300]]
prediction = model.predict(new_house)

print("House Size:", new_house[0][0], "sq ft")
print("Predicted Price: ₹", prediction[0], "lakh")
