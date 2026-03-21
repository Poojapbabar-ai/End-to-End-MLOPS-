"""
Main entry point for the ML project
"""

from src.mlProject.utils.logger import get_logger
from src.mlProject.utils.common import (
    read_yaml, 
    create_directories, 
    save_json
)

logger = get_logger(__name__)


def main():
    """Main function"""
    try:
        logger.info("=" * 60)
        logger.info("Starting ML Project...")
        logger.info("=" * 60)
        
        # Create necessary directories
        directories = [
            "data/raw",
            "data/processed",
            "models",
            "artifacts"
        ]
        logger.info(f"Creating project directories...")
        create_directories(directories)
        
        # Load configuration
        logger.info("Loading configuration...")
        config = read_yaml("config/config.yaml")
        logger.debug(f"Config loaded: {config}")
        
        # Load parameters
        logger.info("Loading parameters...")
        params = read_yaml("params.yaml")
        logger.debug(f"Parameters loaded: {params}")
        
        logger.info("=" * 60)
        logger.info("✓ ML Project initialized successfully!")
        logger.info("=" * 60)
        
    except FileNotFoundError as e:
        logger.error(f"Configuration file not found: {e}")
        return False
    except Exception as e:
        logger.error(f"Error during initialization: {str(e)}")
        return False
    
    return True


if __name__ == "__main__":
    success = main()
    if not success:
        logger.error("Project initialization failed!")
        exit(1)
