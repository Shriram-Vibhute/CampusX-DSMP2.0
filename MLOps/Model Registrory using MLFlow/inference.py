# inference

import mlflow.pyfunc
import numpy as np

data = np.array([1,85,66,29,0,26.6,0.351,31]).reshape(1,-1)

model_name = "diabetes-rf"
model_version = 3

model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}") # Create a uri with model name and version and lode the model by passing that link into pyfunc.load_model() 

print(model.predict(data))