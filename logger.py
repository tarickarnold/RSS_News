import atexit
import toml
import logging.config
import logging.handlers
import os
from config import Config

logger = logging.getLogger(name= __name__)

def setup_logging() -> None:
    dir_name: str = os.path.dirname(p=__file__)
    config_file: str = os.path.join(dir_name, "loggerconfig.toml")
    with open(file= config_file) as f_in:
        config: any = toml.load(f_in)

    logging.config.dictConfig(config)

def main() -> None:
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