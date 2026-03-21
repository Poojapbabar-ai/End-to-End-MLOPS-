"""
Common utility functions with logging
"""

import os
import json
import yaml
from pathlib import Path
from src.mlProject.utils.logger import get_logger

logger = get_logger(__name__)


def read_yaml(yaml_path):
    """
    Read YAML file
    
    Args:
        yaml_path (str): Path to YAML file
        
    Returns:
        dict: Parsed YAML content
    """
    try:
        logger.info(f"Reading YAML file: {yaml_path}")
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        logger.info(f"✓ Successfully loaded YAML from {yaml_path}")
        return data
    except FileNotFoundError:
        logger.error(f"YAML file not found: {yaml_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading YAML file {yaml_path}: {str(e)}")
        raise


def read_json(json_path):
    """
    Read JSON file
    
    Args:
        json_path (str): Path to JSON file
        
    Returns:
        dict: Parsed JSON content
    """
    try:
        logger.info(f"Reading JSON file: {json_path}")
        with open(json_path, 'r') as f:
            data = json.load(f)
        logger.info(f"✓ Successfully loaded JSON from {json_path}")
        return data
    except FileNotFoundError:
        logger.error(f"JSON file not found: {json_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format in {json_path}: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Error reading JSON file {json_path}: {str(e)}")
        raise


def create_directories(paths):
    """
    Create multiple directories
    
    Args:
        paths (list): List of directory paths to create
    """
    try:
        for path in paths:
            os.makedirs(path, exist_ok=True)
            logger.debug(f"Directory created/verified: {path}")
        logger.info(f"✓ Created {len(paths)} directories")
    except Exception as e:
        logger.error(f"Error creating directories: {str(e)}")
        raise


def save_json(data, filepath):
    """
    Save data to JSON file
    
    Args:
        data (dict): Data to save
        filepath (str): Path where to save
    """
    try:
        logger.info(f"Saving data to JSON: {filepath}")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"✓ Data saved successfully to {filepath}")
    except Exception as e:
        logger.error(f"Error saving JSON to {filepath}: {str(e)}")
        raise


def save_yaml(data, filepath):
    """
    Save data to YAML file
    
    Args:
        data (dict): Data to save
        filepath (str): Path where to save
    """
    try:
        logger.info(f"Saving data to YAML: {filepath}")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
        logger.info(f"✓ Data saved successfully to {filepath}")
    except Exception as e:
        logger.error(f"Error saving YAML to {filepath}: {str(e)}")
        raise


if __name__ == "__main__":
    logger.info("Common utilities module loaded")
