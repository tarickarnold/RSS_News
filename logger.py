import atexit
import toml
import logging
import pathlib

logger = logging.getLogger(__name__) 

def setup_logging():
    config_file = pathlib.Path("logging_configs/2-stderr-json-file.json")
    with open(config_file) as f_in:
        config = toml.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level
    
    return filter

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
