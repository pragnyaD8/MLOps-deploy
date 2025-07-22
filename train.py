# train.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split into train and test (optional for this example)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "iris_model.joblib")
print("Model trained and saved as iris_model.joblib")

