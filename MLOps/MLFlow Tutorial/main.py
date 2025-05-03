import mlflow
import mlflow.data
import numpy as np

import mlflow.data
import mlflow.data.pandas_dataset
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
    "max_iter": 25,
    "multi_class": "auto",
    "random_state": 42,
}

# Calculate metrics

with mlflow.start_run():  # Using context manager we dont need to exit_run the mlflow server explicitely.
    mlflow.log_params(params = params)

    # Train the model
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)

    # Predict on the test set
    y_pred = lr.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric(key = "accuracy", value = accuracy)

    train_df_mlflow = mlflow.data.from_pandas(X_train)
    test_df_mlflow = mlflow.data.from_pandas(X_test)

    mlflow.log_input(train_df_mlflow, context = "Training Data")
    mlflow.log_input(test_df_mlflow, context = "Testing Data")