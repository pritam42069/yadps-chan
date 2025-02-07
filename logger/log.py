import logging
from logging.handlers import TimedRotatingFileHandler
class Log:

    formatter = logging.Formatter("%(asctime)s | Module: %(name)s | %(levelname)s | %(message)s")

    def create(self, name, log_file, level=logging.INFO):
        rotate_handler = TimedRotatingFileHandler(filename=log_file, when='h', interval=1, backupCount=2)
        rotate_handler.setFormatter(self.formatter)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(rotate_handler)
        logger.addHandler(console_handler)
        return logger
