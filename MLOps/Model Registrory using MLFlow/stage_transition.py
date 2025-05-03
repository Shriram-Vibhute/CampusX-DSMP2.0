from mlflow.tracking import MlflowClient

# Initialize the MLflow Client
client = MlflowClient()

# Define the model name and version
model_name = "diabetes-rf"
model_version = 3  # Replace with the specific version number you want to transition

# Transition the model version to a new stage
new_stage = "Production"  # Possible values: "None", "Staging", "Production", "Archived"
client.transition_model_version_stage(
    name=model_name,
    version=model_version,
    stage=new_stage,
    archive_existing_versions=True # This is for handling the existing version -> If you provide False, both the model is in production
)

print(f"Model version {model_version} transitioned to {new_stage}")