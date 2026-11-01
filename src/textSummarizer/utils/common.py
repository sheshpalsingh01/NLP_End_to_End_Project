import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """read yaml file and return


    Args:
        path_to_yaml (Path): _description_

    Returns:
        ConfigBox: _description_
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loadded successfully")
            return ConfigBox(content)
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of directories to be created
        verbose (bool, optional): _description_. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
    

