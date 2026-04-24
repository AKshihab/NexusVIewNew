from NexusVIewNew.logger import logger
from NexusVIewNew.custom_exception import InvalidURLException

try:
    raise InvalidURLException()
except Exception as e:
    logger.error(f"An error occurred: {e}")