from deepClassifier.components import DataIngestion
from deepClassifier.config import ConfigurationManager
from deepClassifier import logger

logger.info(f"data ingestion state started.")

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(config=data_ingestion_config)

data_ingestion.download_file()

data_ingestion.unzip_and_clean()

logger.info(f"data ingestion state completed.")