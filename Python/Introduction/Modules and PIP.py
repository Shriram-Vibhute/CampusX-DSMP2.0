# BuiltIn Modules - Came along with python installation
# math
import math
math.sqrt(196)

# keyword
import keyword
print(keyword.kwlist) # Return all the keywords in python

# random
import random
print(random.randint(1,100))

# datetime
import datetime
print(datetime.datetime.now())

# External module - Explictly needs to be installed using pip inorder to use them.
import pandas
df = pandas.read_csv("one.csv")  

# Import the train_test_split function from scikit-learn's model_selection module.
from sklearn.model_selection import train_test_split as tts  # Importing required functions only.

# Example usage of train_test_split to split data into training and testing sets.
X = df[['feature1', 'feature2']]  # Replace with actual feature columns.
y = df['target']  # Replace with the actual target column.

# Splitting the data into training and testing sets with a 80-20 split ratio.
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=42)

# Print the shapes of the resulting datasets to verify the split.
print(f"Training features shape: {X_train.shape}")
print(f"Testing features shape: {X_test.shape}")
print(f"Training target shape: {y_train.shape}")
print(f"Testing target shape: {y_test.shape}")

help('modules') # List of all the modules provided by python including the ones we have installed

'''
pip is the package installer for Python."pip" does not have a universally accepted full form in Python. It allows you to install, manage, and update Python libraries and packages from the Python Package Index (PyPI) and other repositories. Essentially, it's a tool that helps you easily add external libraries to your Python environment, which can provide additional functionality or simplify development tasks.
'''