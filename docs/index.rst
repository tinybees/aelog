Aelog
=====

An simple, async, full package name path, log rotating, different
colored log library.

aelog aims to make using python log as simple as possible. as a result,
it drastically simplifies using python logging.

aelog's design objectives:

-  Make using python log as simple as possible.
-  Output log contains the full package name path.
-  Provide asynchronous log output function, at the same time, contains
   common log output.
-  Output according to the log level to mark the different colors
   separately.
-  Provide a log file rotating, automatic backup.
-  Output to the terminal and file, default output to the terminal, if
   you don't provide the log file path.

Installing aelog
================

-  ``pip install aelog``

init aelog
==========

::

    import aelog

    app = Flask(__name__)

    aelog.init_app(app)
    # or
    aelog.init_app(aelog_access_file='aelog_access_file.log', aelog_error_file='aelog_error_file.log',
                   aelog_console=False)

aelog config
============

List of configuration keys that the aelog extension recognizes:

+------------------------+--------------------------------------------------------+
| configuration key      | the meaning of the configuration key                   |
+========================+========================================================+
| AELOG\_ACCESS\_FILE    | Access file path, default None.                        |
+------------------------+--------------------------------------------------------+
| AELOG\_ERROR\_FILE     | Error file path, default None.                         |
+------------------------+--------------------------------------------------------+
| AELOG\_CONSOLE         | Whether it is output at the terminal, default false.   |
+------------------------+--------------------------------------------------------+
| AELOG\_MAX\_BYTES      | Log file size, default 50M.                            |
+------------------------+--------------------------------------------------------+
| AELOG\_BACKUP\_COUNT   | Rotating file count, default 5.                        |
+------------------------+--------------------------------------------------------+

Usage
=====

simple using, output log to terminal.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import aelog

    aelog.init_app(aelog_console=True)

    def test_aelog_output_console():
        """

        Args:

        Returns:

        """
        aelog.debug("simple debug message", "other message")
        aelog.info("simple info message", "other message")
        aelog.warning("simple warning message", "other message")
        aelog.error("simple error message", "other message")
        aelog.critical("simple critical message", "other message")
        try:
            5 / 0
        except Exception as e:
            aelog.exception(e)

| This will output to the terminal.
| |output_console| - Different levels of logging, different color, the color is
  cyan, green, yellow, red and 'bold\_red,bg\_white' in turn.

output log to file and terminal.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import aelog
    from flask import Flask

    app = Flask(__name__)

    aelog.init_app(app)  # Output to the test.log file and terminal

    def test_aelog_output_file():
        """

        Args:

        Returns:

        """
        aelog.debug("simple debug message", "other message")
        aelog.info("simple info message", "other message")
        aelog.warning("simple warning message", "other message")
        aelog.error("simple error message", "other message")
        aelog.critical("simple critical message", "other message")
        try:
            5 / 0
        except Exception as e:
            aelog.exception(e)

This will output to the test.log file and terminal. |output_file| -
Automatic output is greater than the error information to the
'test\_error.log' file. - Different levels of logging, different color,
the color is cyan, green, yellow, red and 'bold\_red,bg\_white' in turn.

asynchronous output log to file and terminal.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import asyncio
    import aelog
    from sanic import Sanic

    app = Sanic(__name__)

    aelog.init_aelog(app)  # Output to the test.log file and terminal

    async def test_async_output():
        await aelog.async_debug("simple debug message", "other message")
        await aelog.async_info("simple info message", "other message")
        await aelog.async_warning("simple warning message", "other message")
        await aelog.async_error("simple error message", "other message")
        await aelog.async_critical("simple critical message", "other message")
        try:
            5 / 0
        except Exception as e:
            await aelog.async_exception(e)

    if "__name__"=="__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_async_output())

| This will output to the test.log file and terminal. |async_output| -
  Automatic output is greater than the error information to the
  'test\_error.log' file.
| - Different levels of logging, different color, the color is cyan,
  green, yellow, red and 'bold\_red,bg\_white' in turn.

.. |output_console| image:: https://raw.githubusercontent.com/tinybees/aelog/master/docs/output_console.png
.. |output_file| image:: https://raw.githubusercontent.com/tinybees/aelog/master/docs/output_file.png
.. |async_output| image:: https://raw.githubusercontent.com/tinybees/aelog/master/docs/async_output.png

