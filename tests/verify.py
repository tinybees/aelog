#!/usr/bin/env python3
# coding=utf-8

"""
@author: guoyanfeng
@software: PyCharm
@time: 18-3-25 下午7:53
"""

import asyncio

from tests import test_aelog

if __name__ == '__main__':
    test_aelog.test_aelog_output_console()
    test_aelog.test_aelog_output_file()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_aelog.test_async_output())
