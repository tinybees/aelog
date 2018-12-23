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
    aelog.debug("simple debug message")
    aelog.info("simple info message")
    aelog.warning("simple warning message")
    aelog.error("simple error message")
    aelog.critical("simple critical message")
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
    aelog.debug("simple debug message")
    aelog.info("simple info message")
    aelog.warning("simple warning message")
    aelog.error("simple error message")
    aelog.critical("simple critical message")
    try:
        5 / 0
    except Exception as e:
        aelog.exception(e)


async def test_async_output():
    aelog.init_app(aelog_access_file="test.log", aelog_console=True)
    await aelog.async_debug("simple debug message")
    await aelog.async_info("simple info message")
    await aelog.async_warning("simple warning message")
    await aelog.async_error("simple error message")
    await aelog.async_critical("simple critical message")
    try:
        5 / 0
    except Exception as e:
        await aelog.async_exception(e)
