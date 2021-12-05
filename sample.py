import functions
import logging.config

logging.config.fileConfig("logging_debug.conf")

logger = logging.getLogger()

logger.info("info level log")
logger.debug("debug level log")

functions.test_func()