import mlflow
import mlflow.data
import numpy as np

import mlflow.data
import mlflow.data.pandas_dataset
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.model_selection import GridSearchCV


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
    "max_iter": [50, 100, 150, 200],
    "random_state": [1, 2, 3, 4]
}

grid_search = GridSearchCV(LogisticRegression(), params, cv = 5, n_jobs = -1, verbose = 2)

with mlflow.start_run():  # Using context manager we dont need to exit_run the mlflow server explicitely.
    grid_search.fit(X_train, y_train)
    for i in range(len(grid_search.cv_results_['params'])):
        with mlflow.start_run(nested = True):
            mlflow.log_params(grid_search.cv_results_['params'][i])
            mlflow.log_metric("Accuracy", grid_search.cv_results_['mean_test_score'][i])