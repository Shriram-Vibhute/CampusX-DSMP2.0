import mlflow
print(mlflow.get_tracking_uri()) # By default it is File Type
mlflow.set_tracking_uri(uri = "http://127.0.0.1:5000")

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "max_depth": 15,
    "random_state": 42
}

# Calculate metrics
mlflow.set_experiment("decision tree")
# with mlflow.start_run(experiment_id = 123, run_name = "iris_dt_1"):
with mlflow.start_run():  # you can also pass experiment id here as a parameter of already existed Experiment, you can also provide run_name as per your convenience
    mlflow.log_params(params = params)

    # Train the model
    dt = DecisionTreeClassifier(**params)
    dt.fit(X_train, y_train)

    # Predict on the test set
    y_pred = dt.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric(key = "accuracy", value = accuracy)

    # Logging Plots
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize = (6,6))
    sns.heatmap(cm, annot = True, fmt = 'd', cmap = 'Blues')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")

    plt.savefig("Confusion_Matrix.png")
    mlflow.log_artifact("Confusion_Matrix.png")

    # Logging Code
    mlflow.log_artifact(__file__) # You can use pathlib lib for tracking multiple file - This is not recommended because versioning code will be done by git amd github

    # Loggin model
    mlflow.sklearn.log_model(dt, "Decision Tree") # tracking speicific through skleanr helps to provide more info and helps for model serving

    # Setting tags
    mlflow.set_tags(
        {
            "name": "Dexter Morgan",
            "Subject": "MLOps",
            "Tool": "MLFlow"
        }
    )
    