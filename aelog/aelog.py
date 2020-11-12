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
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from logging.config import dictConfig
from typing import Dict, Tuple

from .consts import BACKUP_COUNT, MAX_BYTES
from .log import aelog_config, aelog_default_config

__all__ = ("init_app", "debug", "info", "warning", "error", "critical", "exception", "async_debug",
           "async_info", "async_warning", "async_error", "async_exception", "async_critical")

_pool = ThreadPoolExecutor()


def init_app(app=None, *, aelog_access_file: str = None, aelog_error_file: str = None,
             aelog_console: bool = True, aelog_level: str = "DEBUG",
             aelog_max_bytes: int = MAX_BYTES, aelog_backup_count: int = BACKUP_COUNT):
    """
    init global logging

    if aelog_access_file is none, then output log to the terminal.

    Args:
        app: app 应用
        aelog_access_file: access log full file
        aelog_error_file: error log full file
        aelog_level: log level, default debug
        aelog_console: terminal output log
        aelog_max_bytes: log file max bytes
        aelog_backup_count: backup count
    Returns:

    """
    if app is not None:
        config: Dict = app.config if getattr(app, "config", None) else app.state.config
        aelog_access_file = config.get("AELOG_ACCESS_FILE") or aelog_access_file
        aelog_error_file = config.get("AELOG_ERROR_FILE") or aelog_error_file
        aelog_console = config.get("AELOG_CONSOLE", aelog_console)
        aelog_level = config.get("AELOG_LEVEL") or aelog_level
        aelog_max_bytes = config.get("AELOG_MAX_BYTES") or aelog_max_bytes
        aelog_backup_count = config.get("AELOG_BACKUP_COUNT") or aelog_backup_count

    if aelog_access_file is None:
        aelog_conf = aelog_default_config(loglevel=aelog_level)
    else:
        aelog_conf = aelog_config(aelog_access_file, error_file=aelog_error_file, console=aelog_console,
                                  loglevel=aelog_level, max_bytes=aelog_max_bytes, backup_count=aelog_backup_count)
    dictConfig(aelog_conf)


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
        sio = os.io.StringIO()  # type: ignore
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
