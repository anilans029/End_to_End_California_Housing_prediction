import sys
from Housing.exception import HousingException



import yaml


def read_yaml_file(file_path:str)-> dict:
    
    """
    Readas a YAML file and return the contents as dictionary

    file_path: str
    """
    
    
    try:
        with open(file_path,"rb") as yaml_file:
            content = yaml.safe_load(yaml_file)
            return content
        
    except Exception as e:
        raise HousingException(e,sys) from e