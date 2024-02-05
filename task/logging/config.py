import logging.config
from typing import Any


def _get_log_config() -> dict[str, Any]:
    formatter = "standard"
    handler = "file"
    root_level = "DEBUG"
    main_level = "DEBUG"

    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s [%(levelname)s] %(name)s %(process)d %(thread)d: %(message)s",
            },
            "standard": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            },
            "simple": {
                "format": "[%(levelname)s] %(message)s",
            },
        },
        "handlers": {
            "stdout": {
                "level": "NOTSET",
                "class": "logging.StreamHandler",
                "formatter": formatter,
                "stream": "ext://sys.stdout",
            },
            "file": {
                "level": "NOTSET",
                "class": "logging.FileHandler",
                "formatter": formatter,
                "filename": "portfolio-analysis.log",
                "delay": True,
            },
        },
        "root": {
            "handlers": [handler],
            "level": root_level,
        },
        "loggers": {
            "task": {
                "handlers": [handler],
                "level": main_level,
                "propagate": False,
            },
        },
    }


def configure_logging() -> None:
    log_config = _get_log_config()
    logging.config.dictConfig(log_config)
