"""
Logger module for the ML project
Provides centralized logging configuration
"""

import logging
import os
from datetime import datetime
from pathlib import Path


class Logger:
    """Custom logger class for the ML project"""
    
    _logger = None
    
    @staticmethod
    def get_logger(name=__name__):
        """
        Get or create a logger instance
        
        Args:
            name (str): Logger name (usually __name__)
            
        Returns:
            logging.Logger: Configured logger instance
        """
        if Logger._logger is None:
            Logger._setup_logger(name)
        return Logger._logger
    
    @staticmethod
    def _setup_logger(name):
        """Configure logger with file and console handlers"""
        
        # Create logs directory
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        
        # Create formatters
        detailed_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        simple_format = '%(levelname)s - %(message)s'
        
        formatter_detailed = logging.Formatter(detailed_format)
        formatter_simple = logging.Formatter(simple_format)
        
        # File Handler - Logs everything
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_handler = logging.FileHandler(
            log_dir / f"app_{timestamp}.log"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter_detailed)
        
        # Console Handler - Only info and above
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter_simple)
        
        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        Logger._logger = logger
        logger.info("Logger initialized successfully ✓")
        
        return logger


def get_logger(name=__name__):
    """Convenience function to get logger"""
    return Logger.get_logger(name)
