#!/usr/bin/env python3
# coding=utf-8

"""
@author: guoyanfeng
@software: PyCharm
@time: 18-3-24 下午10:24
"""
import logging
import logging.config
import sys

__all__ = ["init_aelog"]

AELOG_CONFIG_DEFAULTS = {
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
        "aelog_error_console": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "aelog_default",
            "stream": sys.stderr,
        },

    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["aelog_console", "aelog_error_console"]
        }
    }
}


def aelog_config(access_file_name, *, console, max_bytes, backup_count):
    """
    global logging config
    Args:
        access_file_name: access log full filename
        console: terminal output log
        max_bytes: log file max bytes
        backup_count: backup count

    Returns:

    """
    if console:
        handlers = ["aelog_console", "aelog_access_file", "aelog_error_file"]
    else:
        handlers = ["aelog_access_file", "aelog_error_file"]

    pre_file_name, expanded_name = access_file_name.split(".")
    error_file_name = "{}.{}".format("{}_error".format(pre_file_name), expanded_name)

    aelog_config_defaults = {
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
                "level": "INFO",
                "formatter": "aelog_default",
                "filename": access_file_name,
                "maxBytes": max_bytes,
                "backupCount": backup_count,
                "encoding": "utf8"
            },
            "aelog_error_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "aelog_default",
                "filename": error_file_name,
                "maxBytes": max_bytes,
                "backupCount": backup_count,
                "encoding": "utf8"
            }
        },
        "loggers": {
            "": {
                "level": "DEBUG",
                "handlers": handlers
            }
        }
    }
    return aelog_config_defaults


def init_aelog(access_file_name=None, console=False, max_bytes=50 * 1024 * 1024, backup_count=5):
    """
    init global logging

    if access_file_name is none, then output log to the terminal.

    Args:
        access_file_name: access log full filename
        console: terminal output log
        max_bytes: log file max bytes
        backup_count: backup count

    Returns:

    """
    if access_file_name is None:
        aelog_conf = AELOG_CONFIG_DEFAULTS
    else:
        aelog_conf = aelog_config(access_file_name, console=console, max_bytes=max_bytes, backup_count=backup_count)
    logging.config.dictConfig(aelog_conf)
    init_aelog.init_flag = True
