# file_path="/config/workspace/aps_failure_training_set1.csv"
from src.data_access.sensor_data import SensorData
from src.constant import DATA_INGESTION_COLLECTION_NAME
from src.utils.main_utils import read_yaml_file
import os

def set_env_variable(env_file_path):

    if os.getenv('MONGO_DB_URL',None) is None:
        env_config = read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']


if __name__=='__main__':
    data_file_path="/aps_failure_training_set1.csv"
    env_file_path='/env.yaml'
    set_env_variable(env_file_path)
    print( os.environ['MONGO_DB_URL'])
    sd = SensorData()
    if DATA_INGESTION_COLLECTION_NAME in sd.mongo_client.database.list_collection_names():
        sd.mongo_client.database[DATA_INGESTION_COLLECTION_NAME].drop()
    sd.save_csv_file(file_path=data_file_path,collection_name=DATA_INGESTION_COLLECTION_NAME)

