import yaml
from .logger import logger


def load_config():
    try:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        logger.info("Successfully loaded config.yaml")
        return config
    except Exception as e:
        logger.error(f"Error loading config.yaml: {e}")
        raise
