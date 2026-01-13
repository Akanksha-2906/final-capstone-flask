import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("dataset.csv")

# X = data.drop("target", axis=1)
# y = data["target"]
# Features and target
# X = df[["f1", "f2", "f3"]]   #these should match CSV columns
# y = df["target"]
X = df[["experience", "projects", "certifications"]]   #these should match CSV columns
y = df["salary"]


model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully")
