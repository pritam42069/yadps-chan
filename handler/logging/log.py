import logging
import time


class Log:

    log_format = logging.Formatter("%(asctime)s | Module: %(name)s | %(levelname)s | %(message)s")

    def create(self, name, log_file, level=logging.INFO):
        log_file_handler = logging.FileHandler(log_file + time.strftime("-%Y-%m-%d"))
        log_file_handler.setFormatter(self.log_format)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.log_format)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(log_file_handler)
        logger.addHandler(console_handler)
        return logger


