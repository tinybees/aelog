#!/usr/bin/env python3
# coding=utf-8

"""
@author: guoyanfeng
@software: PyCharm
@time: 18-3-26 上午11:37
"""

import aelog


def test_get_logger():
    """

    Args:

    Returns:

    """
    aelog.init_app(aelog_access_file="test.log", aelog_console=True)
    logger = aelog.get_logger()
    logger.debug("simple debug message")
    logger.info("simple info message")
    logger.warning("simple warning message")
    logger.error("simple error message")
    logger.critical("simple critical message")
    try:
        5 / 0
    except Exception as e:
        logger.exception(e)


def test_aelog_output_console():
    """

    Args:

    Returns:

    """
    aelog.init_app(aelog_console=True)
    aelog.debug("simple debug message", "other message", 1, [1, 2, 3])
    aelog.info("simple info message", "other message", 2, (1, 2, 3))
    aelog.warning("simple warning message", "other message", 3, {1, 2, 3})
    aelog.error("simple error message", "other message", 4, {1: 1, 2: 2, 3: 3})
    aelog.critical("simple critical message", "other message", 5, classmethod)
    try:
        5 / 0
    except Exception as e:
        aelog.exception(e)


def test_aelog_output_file():
    """

    Args:

    Returns:

    """
    aelog.init_app(aelog_access_file="test.log", aelog_console=True)
    aelog.debug("simple debug message", "other message", 1, [6, 2, 3])
    aelog.info("simple info message", "other message", 1, [6, 2, 3])
    aelog.warning("simple warning message", "other message", 1, [6, 2, 3])
    aelog.error("simple error message", "other message", 1, [1, 2, 3])
    aelog.critical("simple critical message", "other message", 1, [1, 2, 3])
    try:
        5 / 0
    except Exception as e:
        aelog.exception(e)


async def test_async_output():
    aelog.init_app(aelog_access_file="test.log", aelog_console=True)
    await aelog.async_debug("simple debug message", "other message", 3, {1, 2})
    await aelog.async_info("simple info message", "other message", 4, {3: 3})
    await aelog.async_warning("simple warning message", "other message", 4, {3: 3})
    await aelog.async_error("simple error message", "other message", 4, {3: 3})
    await aelog.async_critical("simple critical message", "other message", 4, {3: 3})
    try:
        5 / 0
    except Exception as e:
        await aelog.async_exception(e)
