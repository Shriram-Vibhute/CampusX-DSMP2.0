import mlflow
from mlflow.models import infer_signature
mlflow.autolog()
print(mlflow.get_tracking_uri())
mlflow.set_tracking_uri(uri = "http://127.0.0.1:5000")

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Load the Iris dataset
data = datasets.load_iris(as_frame=True)
X = data['data']
y = data['target']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "solver": "lbfgs",
    "max_iter": 500,
    "multi_class": "auto",
    "random_state": 42,
}

# Calculate metrics

with mlflow.start_run():  # Using context manager we dont need to exit_run the mlflow server explicitely.
    # mlflow.log_params(params = params)
    
    # Train the model
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)

    # Infer the model signature
    signature = infer_signature(X_train, lr.predict(X_train))

    # Predict on the test set
    y_pred = lr.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    # mlflow.log_metric(key = "accuracy", value = accuracy)