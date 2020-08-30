#!/usr/bin/env python3
# coding=utf-8

"""
@author: guoyanfeng
@software: PyCharm
@time: 18-3-24 下午10:24
"""
import sys

__all__ = ["aelog_config", "aelog_default_config"]


def aelog_default_config(loglevel="DEBUG"):
    """
    default logging config
    Args:
        loglevel: log level, default debug
    Returns:

    """
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
                "level": "DEBUG",
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


def aelog_config(access_file, *, console, max_bytes, backup_count, error_file=None, loglevel="DEBUG"):
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
            }
        },
        "handlers": {
            "aelog_console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "aelog_default",
                "stream": sys.stdout,
            },
            "aelog_access_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
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
            }
        },
        "loggers": {
            "": {
                "level": loglevel,
                "handlers": handlers
            }
        }
    }
    return log_config
