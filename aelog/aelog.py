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
from concurrent.futures import ThreadPoolExecutor
from logging import Logger

from .log import init_aelog

__all__ = ["get_logger", "debug", "info", "warning", "error", "critical", "exception",
           "async_debug", "async_info", "async_warning", "async_error", "async_exception", "async_critical"]

pool = ThreadPoolExecutor()


def get_logger() -> Logger:
    """
    get logger object, If the aelog has no initialize, call init_aelog() and output to the terminal.
    Args:

    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    return logging.getLogger(caller_module.__name__)


def debug(msg, *args, **kwargs):
    """
    Log a message with severity 'DEBUG' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    logger.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """
    Log a message with severity 'INFO' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    logger.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    """
    Log a message with severity 'WARNING' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    logger.warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    logger.error(msg, *args, **kwargs)


def critical(msg, *args, **kwargs):
    """
    Log a message with severity 'CRITICAL' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    logger.critical(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger, with exception information. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    logger.exception(msg, *args, exc_info=True, **kwargs)


async def async_debug(msg, *args, **kwargs):
    """
    Log a message with severity 'DEBUG' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    await asyncio.wrap_future(pool.submit(logger.debug, msg, *args, **kwargs))


async def async_info(msg, *args, **kwargs):
    """
    Log a message with severity 'INFO' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    await asyncio.wrap_future(pool.submit(logger.info, msg, *args, **kwargs))


async def async_warning(msg, *args, **kwargs):
    """
    Log a message with severity 'WARNING' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    await asyncio.wrap_future(pool.submit(logger.warning, msg, *args, **kwargs))


async def async_error(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    await asyncio.wrap_future(pool.submit(logger.error, msg, *args, **kwargs))


async def async_critical(msg, *args, **kwargs):
    """
    Log a message with severity 'CRITICAL' on the root logger. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    await asyncio.wrap_future(pool.submit(logger.critical, msg, *args, **kwargs))


async def async_exception(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger, with exception information. If the aelog has no initialize,
    call init_aelog() and output to the terminal.
    Args:
        msg, *args, **kwargs
    Returns:

    """
    if not getattr(init_aelog, "init_flag"):
        init_aelog()
    caller_module = inspect.getmodule(inspect.currentframe().f_back)
    logger = logging.getLogger(caller_module.__name__)
    await asyncio.wrap_future(pool.submit(logger.exception, msg, *args, exc_info=True, **kwargs))
