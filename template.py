import os
from pathlib import Path

files_list = [ 
    "src/__init__.py",
    "src/exceptions.py",
    "src/logger.py",
    "src/cloud_storage/__init__.py",
    "src/cloud_storage/s3_syncer.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/data_validation.py",
    "src/components/model_evaluation.py",
    "src/components/model_pusher.py",
    "src/components/model_trainer.py",
    "src/configuration/__init__.py",
    "src/configuration/mongodb_connection.py",
    "src/constant/__init__.py",
    "src/data_access/__init__.py",
    "src/data_access/sensor_data.py",
    "src/entity/__init__.py",
    "src/entity/artifact_entity.py",
    "src/entity/config_entity.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/main_utils.py",
    "config/schema.yaml"

]

for file in files_list:
    file_path = Path(file)

    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    print(f"Created directory: {filedir}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass

    print(f"Created file: {filename}")