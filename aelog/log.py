#!/usr/bin/env python3
# coding=utf-8

"""
@author: guoyanfeng
@software: PyCharm
@time: 18-3-24 下午10:24
"""
import sys
# noinspection PyProtectedMember
from logging import _nameToLevel
from typing import Dict

from .consts import BACKUP_COUNT, MAX_BYTES

__all__ = ["aelog_config", "aelog_default_config", "sanic_log_config"]


def verify_loglevel(loglevel: str) -> str:
    """
    校验loglevel是否正确
    Args:
        loglevel: log level name
    Returns:

    """
    level_name = list(_nameToLevel.keys())
    loglevel = loglevel.upper()
    if loglevel not in level_name:
        raise ValueError(f"参数loglevel必须为{level_name}中的一个")
    return loglevel


def aelog_default_config(loglevel: str = "DEBUG") -> Dict:
    """
    default logging config
    Args:
        loglevel: log level, default debug
    Returns:

    """
    loglevel = verify_loglevel(loglevel)
    return {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "aelog_default": {
                "format": '%(asctime)s %(log_color)s [%(levelname)s] %(name)s [%(funcName)s %(lineno)d]: %(message)s',
                "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
                "class": "colorlog.ColoredFormatter",
                "reset": True,
                "log_colors": {
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red,bg_white',

                },
            }
        },
        "handlers": {
            "aelog_console": {
                "class": "logging.StreamHandler",
                "formatter": "aelog_default",
                "stream": sys.stdout,
            }
        },
        "loggers": {
            "": {
                "level": loglevel,
                "handlers": ["aelog_console"]
            }
        }
    }


def aelog_config(access_file: str, *, error_file: str = None, console: bool = True, loglevel: str = "DEBUG",
                 max_bytes: int = MAX_BYTES, backup_count: int = BACKUP_COUNT) -> Dict:
    """
    global logging config
    Args:
        access_file: access log full file
        console: terminal output log
        max_bytes: log file max bytes
        backup_count: backup count
        error_file: error log full file
        loglevel: log level, default debug
    Returns:

    """
    loglevel = verify_loglevel(loglevel)
    if console:
        handlers = ["aelog_console", "aelog_access_file", "aelog_error_file"]
    else:
        handlers = ["aelog_access_file", "aelog_error_file"]
    access_file = access_file if access_file.endswith(".log") else "{}.{}".format(access_file, "log")
    if error_file is None:
        pre_file_name, expanded_name = access_file.rsplit(".")
        error_file = "{}.{}".format("{}_error".format(pre_file_name), expanded_name)
    else:
        error_file = error_file if error_file.endswith(".log") else "{}.{}".format(error_file, "log")

    log_config = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "aelog_default": {
                "format": '%(asctime)s %(log_color)s [%(levelname)s] %(name)s [%(funcName)s %(lineno)d]: %(message)s',
                "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
                "class": "colorlog.ColoredFormatter",
                "reset": True,
                "log_colors": {
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red,bg_white',
                },
            },
        },
        "handlers": {
            "aelog_console": {
                "class": "logging.StreamHandler",
                "formatter": "aelog_default",
                "stream": sys.stdout,
            },
            "aelog_access_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "aelog_default",
                "filename": access_file,
                "maxBytes": max_bytes,
                "backupCount": backup_count,
                "encoding": "utf8"
            },
            "aelog_error_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "aelog_default",
                "filename": error_file,
                "maxBytes": max_bytes,
                "backupCount": backup_count,
                "encoding": "utf8"
            },
        },
        "loggers": {
            "": {
                "level": loglevel,
                "handlers": handlers
            }
        }
    }
    return log_config


def sanic_log_config(access_file: str, *, error_file: str = None, console: bool = True, loglevel: str = "DEBUG",
                     max_bytes: int = MAX_BYTES, backup_count: int = BACKUP_COUNT) -> Dict:
    """
    global logging config
    Args:
        access_file: access log full file
        console: terminal output log
        max_bytes: log file max bytes
        backup_count: backup count
        error_file: error log full file
        loglevel: log level, default debug
    Returns:

    """
    loglevel = verify_loglevel(loglevel)
    if access_file.endswith(".log"):
        access_file = access_file
    else:
        access_file = "{}.{}".format(access_file, "log")

    if error_file is None:
        pre_file_name, expanded_name = access_file.rsplit(".")
        error_file = "{}.{}".format("{}_error".format(pre_file_name), expanded_name)
    else:
        error_file = error_file if error_file.endswith(".log") else "{}.{}".format(error_file, "log")

    log_config = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "generic": {
                "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
                "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
                "class": "logging.Formatter",
            },
            "access": {
                "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: "
                          + "%(request)s %(message)s %(status)d %(byte)d",
                "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
                "class": "logging.Formatter",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "generic",
                "stream": sys.stdout,
            },
            "access_console": {
                "class": "logging.StreamHandler",
                "formatter": "access",
                "stream": sys.stdout,
            },
            "access_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "access",
                "filename": access_file,
                "maxBytes": max_bytes,
                "backupCount": backup_count,
                "encoding": "utf8"
            },
            "error_console": {
                "class": "logging.StreamHandler",
                "formatter": "generic",
                "stream": sys.stdout,
            },
            "error_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "generic",
                "filename": error_file,
                "maxBytes": max_bytes,
                "backupCount": backup_count,
                "encoding": "utf8"
            },
        },
        "loggers": {
            "sanic.root": {
                "level": loglevel,
                "handlers": ["console"] if console else []},
            "sanic.error": {
                "level": loglevel,
                "handlers": ["error_file", "error_console"] if console else ["error_file"],
                "qualname": "sanic.error",
            },
            "sanic.access": {
                "level": "INFO",
                "handlers": ["access_file", "access_console"] if console else ["access_file"],
                "qualname": "sanic.access",
            },
        }
    }

    return log_config
