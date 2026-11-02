from src.textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textSummarizer.utils.common import read_yaml,create_directore
from src.textSummarizer.entity import DataIngestionConfig, DataTransformationConfig
import os
from pathlib import Path


class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path= PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directore([self.config.artifact_root])
        
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config= self.config.data_ingestion
        create_directore([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file= config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
            config = self.config.data_transformation
            
            create_directore([config.root_dir])
            
            data_transformation_config = DataTransformationConfig(
                root_dir=Path(config.root_dir),
                data_path=Path(config.data_path),
                tokenizer_path=Path(config.tokenizer_name)
            )
            
            return data_transformation_config
    
