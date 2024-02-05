import logging

from task.logging.config import configure_logging

LOGGER = logging.getLogger(__package__)


def main() -> None:
    configure_logging()
    LOGGER.info("hello world")


if __name__ == "__main__":
    main()
