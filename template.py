import os
from pathlib import Path

list_of_files=[
    ".github/workflows",
    "scr/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion/__init__.py",
    "src/components/data_transformation/__init__.py",
    "src/components/model_trainer.py",  # model on train data
    "src/components/model_evaluation.py", # model on test data
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py", # training pipeline
    "src/pipeline/prediction_pipeline.py", # inference pipeline
    "src/utils/__init__.py"
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py"
    "tests/unit/__init__.py",  # unit testing 
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.config",
    "pyproject.tml",
    "tox.ini",
    "experiment/experiments.ipynb",

]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        #logging.info(f"Creating directory: {filedir} for : {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass


