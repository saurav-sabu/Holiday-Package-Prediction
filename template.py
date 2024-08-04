import os
import sys
from pathlib import Path

# List of files to be created
list_of_files = [
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
    "artifacts/.gitkeep",
    "notebooks/data/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/utils.py",
    "src/logger.py",
    "src/exception.py"
]

# Loop through each file path in the list
for file_path in list_of_files:
    file_path = Path(file_path) # Convert to a Path object for easier manipulation
    
    file_dir,file_name = os.path.split(file_path) # Split into directory and file name

    # Create the directory if it does not exist
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)

    
    # Create the file if it does not exist or if it is empty
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) ==0):
        with open(file_path,"w") as f:
            pass # Create an empty file
    else:
        print(f"File already exists: {file_path}") # Print a message if the file already exists

    