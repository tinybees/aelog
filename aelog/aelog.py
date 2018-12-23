#!/usr/bin/env python3
# coding=utf-8

"""
@author: guoyanfeng
@software: PyCharm
@time: 18-3-24 下午10:23
"""

import asyncio
import inspect
import logging
import os
import traceback
import warnings
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from logging import Logger
from logging.config import dictConfig

from .log import *

__all__ = ("init_app", "init_aelog", "get_logger", "debug", "info", "warning", "error", "critical", "exception",
           "async_debug", "async_info", "async_warning", "async_error", "async_exception", "async_critical")

_pool = ThreadPoolExecutor()


def init_aelog(access_file_name=None, console=False, max_bytes=50 * 1024 * 1024, backup_count=5, error_file=None):
    """
    init global logging

    if access_file is none, then output log to the terminal.

    Args:
        access_file_name: access log full file
        console: terminal output log
        max_bytes: log file max bytes
        backup_count: backup count
        error_file: error log full file
    Returns:

    """
    warnings.warn("`init_aelog` option is deprecated in version 1.0.3.  Use `aelog.init_app` instead.",
                  DeprecationWarning)
    init_app(aelog_access_file=access_file_name, aelog_console=console, aelog_max_bytes=max_bytes,
             aelog_backup_count=backup_count, aelog_error_file=error_file)


def init_app(app=None, *, aelog_access_file=None, aelog_console=False, aelog_max_bytes=50 * 1024 * 1024,
             aelog_backup_count=5, aelog_error_file=None):
    """
    init global logging

    if aelog_access_file is none, then output log to the terminal.

    Args:
        app: app 应用
        aelog_access_file: access log full file
        aelog_console: terminal output log
        aelog_max_bytes: log file max bytes
        aelog_backup_count: backup count
        aelog_error_file: error log full file
    Returns:

    """
    if app is not None:
        aelog_access_file = app.config.get("AELOG_ACCESS_FILE", None) or aelog_access_file
        aelog_console = app.config.get("AELOG_CONSOLE", None) or aelog_console
        aelog_max_bytes = app.config.get("AELOG_MAX_BYTES", None) or aelog_max_bytes
        aelog_backup_count = app.config.get("AELOG_BACKUP_COUNT", None) or aelog_backup_count
        aelog_error_file = app.config.get("AELOG_ERROR_FILE", None) or aelog_error_file

    if aelog_access_file is None:
        aelog_conf = AELOG_CONFIG_DEFAULTS
    else:
        aelog_conf = aelog_config(aelog_access_file, console=aelog_console, max_bytes=aelog_max_bytes,
                                  backup_count=aelog_backup_count, error_file=aelog_error_file)
    dictConfig(aelog_conf)
    init_app.init_flag = True


def get_logger() -> Logger:
    """
    get logger object, If the aelog has no initialize, call init_aelog() and output to the terminal.
    Args:

    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    return logging.getLogger(caller_module.__name__ if caller_module else "")


def find_caller(caller_frame, stack_info=False):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    if hasattr(caller_frame, "f_code"):
        co = caller_frame.f_code
    else:
        return "(unknown file)", 0, "(unknown function)", None

    sinfo = None
    if stack_info:
        sio = os.io.StringIO()
        sio.write('Stack (most recent call last):\n')
        traceback.print_stack(caller_frame, file=sio)
        sinfo = sio.getvalue()
        if sinfo[-1] == '\n':
            sinfo = sinfo[:-1]
        sio.close()
    return co.co_filename, caller_frame.f_lineno, co.co_name, sinfo


def debug(msg, *args, **kwargs):
    """
    Log a message with severity 'DEBUG' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """
    Log a message with severity 'INFO' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    """
    Log a message with severity 'WARNING' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.error(msg, *args, **kwargs)


def critical(msg, *args, **kwargs):
    """
    Log a message with severity 'CRITICAL' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.critical(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger, with exception information. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.exception(msg, *args, exc_info=msg, **kwargs)


async def async_debug(msg, *args, **kwargs):
    """
    Log a message with severity 'DEBUG' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.debug, msg, *args, **kwargs))


async def async_info(msg, *args, **kwargs):
    """
    Log a message with severity 'INFO' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.info, msg, *args, **kwargs))


async def async_warning(msg, *args, **kwargs):
    """
    Log a message with severity 'WARNING' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.warning, msg, *args, **kwargs))


async def async_error(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.error, msg, *args, **kwargs))


async def async_critical(msg, *args, **kwargs):
    """
    Log a message with severity 'CRITICAL' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.critical, msg, *args, **kwargs))


async def async_exception(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger, with exception information. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.exception, msg, *args, exc_info=msg, **kwargs))
