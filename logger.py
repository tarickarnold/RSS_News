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
    logging.basicConfig(level="INFO")
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
