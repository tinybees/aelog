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
# noinspection PyProtectedMember
from logging import Logger, _nameToLevel
from logging.config import dictConfig
from typing import Tuple

from .log import *

__all__ = ("init_app", "get_logger", "debug", "info", "warning", "error", "critical", "exception",
           "async_debug", "async_info", "async_warning", "async_error", "async_exception", "async_critical")

_pool = ThreadPoolExecutor()


def init_app(app=None, *, aelog_access_file=None, aelog_error_file=None, loglevel="DEBUG",
             aelog_console=False, aelog_max_bytes=50 * 1024 * 1024, aelog_backup_count=5):
    """
    init global logging

    if aelog_access_file is none, then output log to the terminal.

    Args:
        app: app 应用
        aelog_access_file: access log full file
        aelog_error_file: error log full file
        loglevel: log level, default debug
        aelog_console: terminal output log
        aelog_max_bytes: log file max bytes
        aelog_backup_count: backup count
    Returns:

    """
    level_name = list(_nameToLevel.keys())
    loglevel = loglevel.upper()
    if loglevel not in level_name:
        raise ValueError(f"参数loglevel必须为{level_name}中的一个")

    if app is not None:
        aelog_access_file = app.config.get("AELOG_ACCESS_FILE", None) or aelog_access_file
        aelog_error_file = app.config.get("AELOG_ERROR_FILE", None) or aelog_error_file
        aelog_console = app.config.get("AELOG_CONSOLE", None) or aelog_console
        aelog_max_bytes = app.config.get("AELOG_MAX_BYTES", None) or aelog_max_bytes
        aelog_backup_count = app.config.get("AELOG_BACKUP_COUNT", None) or aelog_backup_count

    if aelog_access_file is None:
        aelog_conf = aelog_default_config(loglevel=loglevel)
    else:
        aelog_conf = aelog_config(aelog_access_file, console=aelog_console, max_bytes=aelog_max_bytes,
                                  backup_count=aelog_backup_count, error_file=aelog_error_file, loglevel=loglevel)
    dictConfig(aelog_conf)
    init_app.init_flag = True


def get_logger() -> Logger:
    """
    get logger object, If the aelog has no initialize, call init_aelog() and output to the terminal.
    Args:

    Returns:

    """
    warnings.warn("`get_logger` option is deprecated in version 1.0.5.  Use `aelog` instead.",
                  DeprecationWarning)
    if not getattr(init_app, "init_flag", None):
        init_app()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    return logging.getLogger(caller_module.__name__ if caller_module else "")


def find_caller(caller_frame, stack_info=False) -> Tuple:
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


def debug(msg, *args, sep=' '):
    """
    Log a message with severity 'DEBUG' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.debug(f"{sep}".join(str(val) for val in (msg, *args)))


def info(msg, *args, sep=' '):
    """
    Log a message with severity 'INFO' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.info(f"{sep}".join(str(val) for val in (msg, *args)))


def warning(msg, *args, sep=' '):
    """
    Log a message with severity 'WARNING' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.warning(f"{sep}".join(str(val) for val in (msg, *args)))


def error(msg, *args, sep=' '):
    """
    Log a message with severity 'ERROR' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.error(f"{sep}".join(str(val) for val in (msg, *args)))


def critical(msg, *args, sep=' '):
    """
    Log a message with severity 'CRITICAL' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.critical(f"{sep}".join(str(val) for val in (msg, *args)))


def exception(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger, with exception information. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        kwargs: 其他参数
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    logger.exception(msg, *args, exc_info=msg, **kwargs)


async def async_debug(msg, *args, sep=' '):
    """
    Log a message with severity 'DEBUG' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.debug, f"{sep}".join(str(val) for val in (msg, *args))))


async def async_info(msg, *args, sep=' '):
    """
    Log a message with severity 'INFO' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.info, f"{sep}".join(str(val) for val in (msg, *args))))


async def async_warning(msg, *args, sep=' '):
    """
    Log a message with severity 'WARNING' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.warning, f"{sep}".join(str(val) for val in (msg, *args))))


async def async_error(msg, *args, sep=' '):
    """
    Log a message with severity 'ERROR' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.error, f"{sep}".join(str(val) for val in (msg, *args))))


async def async_critical(msg, *args, sep=' '):
    """
    Log a message with severity 'CRITICAL' on the root logger. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        sep: 多个消息的分隔符, 默认为一个空格.
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.critical, f"{sep}".join(str(val) for val in (msg, *args))))


async def async_exception(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger, with exception information. If the aelog has no initialize,
    call init_app() and output to the terminal.
    Args:
        msg: 要打印消息内容
        args: 要打印的其他消息内容
        kwargs: 其他参数
    Returns:

    """
    caller_frame = inspect.currentframe().f_back
    caller_module = inspect.getmodule(caller_frame)
    logger = logging.getLogger(caller_module.__name__ if caller_module else "")
    logger.findCaller = partial(find_caller, caller_frame)
    await asyncio.wrap_future(_pool.submit(logger.exception, msg, *args, exc_info=msg, **kwargs))
