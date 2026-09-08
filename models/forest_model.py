import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("data/forest_data.csv")

data["condition"] = data["canopy_percent"].apply(
    lambda x: "Low" if x < 30 else "Healthy"
)

X = data[["canopy_percent"]]
y = data["condition"]

model = DecisionTreeClassifier()
model.fit(X, y)

print("🌲 SylvaSense AI Model")
print("----------------------")

canopy = float(input("Enter canopy coverage (%): "))

prediction = model.predict([[canopy]])

print("Predicted Forest Condition:", prediction[0])