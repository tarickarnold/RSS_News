import toml
import logging
import logging.config
import os

logger = logging.getLogger(__name__) 

def setup_logging():
    config_dir = os.path.dirname(__file__)
    config_file = os.path.join(config_dir, "loggerconfig.toml")
    with open(config_file) as f_in:
        config = toml.load(f_in)

    logging.config.dictConfig(config)

def main():
    setup_logging()
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")

if __name__ == "__main__":
    main()

import toml
import logging
import logging.config
import logging.handlers
import os

logger = logging.getLogger(__name__) 

class Logger:
    def __init__(self) -> None:
        self.logger = logging.getLogger('Logger')
        self.logger.info('creating an instance of Logger')

    def setup_logging() -> None:
        config_dir = os.path.dirname(__file__)
        config_file = os.path.join(config_dir, "loggerconfig.toml")
        with open(config_file) as f_in:
            config = toml.load(f_in)
        logging.config.dictConfig(config)

def main() -> None:
    Logger.setup_logging()
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")

if __name__ == "__main__":
    main()