import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig
from src.textSummarizer.config.configuration import ConfigurationManager


config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        
    
    def download_file(self):
        os.makedirs(data_ingestion_config.root_dir, exist_ok=True)

        if not os.path.isfile(data_ingestion_config.local_data_file):
            request.urlretrieve(
                str(data_ingestion_config.source_url),
                str(data_ingestion_config.local_data_file)
    )
            logger.info(f"File download sucessfully")
        else:
            logger.info(f"File already exits")
            
    def extract_zip_file(self):
        """
        Zip_file_path: str
        Extract the zip file into the data dir directory
        function returns None
        
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        
            
        