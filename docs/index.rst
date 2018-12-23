.. role:: raw-html-m2r(raw)
   :format: html


Aelog
=====

An simple, async, full package name path, log rotating, different colored log library.

aelog aims to make using python log as simple as possible. as a result, it drastically
simplifies using python logging.

aelog's design objectives:


* Make using python log as simple as possible.
* Output log contains the full package name path.
* Provide asynchronous log output function, at the same time, contains common log output.
* Output according to the log level to mark the different colors separately.
* Provide a log file rotating, automatic backup.
* Output to the terminal and file, default output to the terminal, if you don't provide the log file path.

Installing aelog
================


* ``pip install aelog``


init aelog
==========

.. code-block::

   import aelog

   app = Flask(__name__)

   aelog.init_app(app)
   # or
   aelog.init_app(aelog_access_file='aelog_access_file.log', aelog_error_file='aelog_error_file.log',
                  aelog_console=False)

aelog config
============

List of configuration keys that the aelog extension recognizes:

.. list-table::
   :header-rows: 1

   * - configuration key
     - the meaning of the configuration key
   * - AELOG_ACCESS_FILE
     - Access file path, default None.
   * - AELOG_ERROR_FILE
     - Error file path, default None.
   * - AELOG_CONSOLE
     - Whether it is output at the terminal, default false.
   * - AELOG_MAX_BYTES
     - Log file size, default 50M.
   * - AELOG_BACKUP_COUNT
     - Rotating file count, default 5.


Usage
=====

simple using, not initialized.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   import aelog

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

This will output to the terminal.\ :raw-html-m2r:`<br>`

.. image:: https://raw.githubusercontent.com/tinybees/aelog/master/docs/output_console.png
   :target: https://raw.githubusercontent.com/tinybees/aelog/master/docs/output_console.png
   :alt: console



* Different levels of logging, different color, the color is cyan, green, yellow, red and 'bold_red,bg_white' in turn.

To initialize, output log to file and terminal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   import aelog
   from flask import Flask

   app = Flask(__name__)

   aelog.init_app(app)  # Output to the test.log file and terminal

   def test_aelog_output_file():
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

This will output to the test.log file and terminal.

.. image:: https://raw.githubusercontent.com/tinybees/aelog/master/docs/output_file.png
   :target: https://raw.githubusercontent.com/tinybees/aelog/master/docs/output_file.png
   :alt: console



* Automatic output is greater than the error information to the 'test_error.log' file.
* Different levels of logging, different color, the color is cyan, green, yellow, red and 'bold_red,bg_white' in turn.

To initialize, asynchronous output log to file and terminal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   import asyncio
   import aelog
   from sanic import Sanic

   app = Sanic(__name__)

   aelog.init_aelog(app)  # Output to the test.log file and terminal

   async def test_async_output():
       await aelog.async_debug("simple debug message")
       await aelog.async_info("simple info message")
       await aelog.async_warning("simple warning message")
       await aelog.async_error("simple error message")
       await aelog.async_critical("simple critical message")
       try:
           5 / 0
       except Exception as e:
           await aelog.async_exception(e)

   if "__name__"=="__main__":
       loop = asyncio.get_event_loop()
       loop.run_until_complete(test_async_output())

This will output to the test.log file and terminal.

.. image:: https://raw.githubusercontent.com/tinybees/aelog/master/docs/async_output.png
   :target: https://raw.githubusercontent.com/tinybees/aelog/master/docs/async_output.png
   :alt: console



* Automatic output is greater than the error information to the 'test_error.log' file.
* Different levels of logging, different color, the color is cyan, green, yellow, red and 'bold_red,bg_white' in turn.


Changelog
=========

[1.0.2] - 2018-12-23
^^^^^^^^^^^^^^^^^^^^

Added
~~~~~


* 增加init_app初始化方法，可以直接传入app初始化（参考类flask扩展的方式）
* 增加指定错误日志文件的功能，如没有指定则和老版本处理方式相同

Changed
~~~~~~~


* 修改init_aelog实现方式，增加警告内容
* 增加log文件的校验，保证是log结尾的日志文件
* 重构部分内容

[1.0.1] - 2018-03-28
^^^^^^^^^^^^^^^^^^^^

Added
~~~~~


* 测试完成，发布到pypi

Changed
~~~~~~~


* 修改直接在终端执行报错的问题

[1.0.0] - 2018-03-25
^^^^^^^^^^^^^^^^^^^^

Added
~~~~~


* Make using python log as simple as possible.
* Output log contains the full package name path.
* Provide asynchronous log output function, at the same time, contains common log output.
* Output according to the log level to mark the different colors separately.
* Provide a log rotating, automatic backup.
* Default output to the terminal, if you don't provide the log file path.
* Edit readme,push to pypi, and so on.
