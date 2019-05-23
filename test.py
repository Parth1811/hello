import logging
from datetime import datetime


logging.basicConfig(filename = 'log.txt', level = logging.DEBUG)
logger = logging.getLogger()
logger.info("Starting log for " + str(datetime.now()))
