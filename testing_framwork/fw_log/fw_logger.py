'''
    This class encapsulate the logger
'''
import logging


class FwLogger:

    logger = None
    name = "main_app"

    def __init__(self, log_name = name):
        self.logger = logging.getLogger(log_name)
        self.__format__("%(asctime)s | %(levelname)s | %(message)s")

    def log_entry(self, text, args=None, kwargs=None):
        self.logger.info(text)


logApp = FwLogger()
logApp.log_entry("Abc")