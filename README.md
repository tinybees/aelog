# Aelog
An simple, async, full package name path, log rotating, different colored log library.

aelog aims to make using python log as simple as possible. as a result, it drastically 
simplifies using python logging.

aelog's design objectives:

- Make using python log as simple as possible.
- Output log contains the full package name path.
- Provide asynchronous log output function, at the same time, contains common log output.
- Output according to the log level to mark the different colors separately.
- Provide a log rotating, automatic backup.
- Default output to the terminal, if you don't provide the log file path.

# Installing aelog
- ```pip install aelog```

# Usage
### simple using.
```
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
```
This will output to the terminal.
![console](docs/output_console.png)

### To initialize, output log to file and terminal.
```
import aelog

aelog.init_aelog("test.log", True)

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
```
This will output to the test.log, test_error.log file and terminal.
Automatic output is greater than the error information to the 'test_error.log' files.
![console](docs/output_file.png)

### To initialize, asynchronous output log to file and terminal.
```
import asyncio
import aelog

aelog.init_aelog("test.log", True)

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
```
This will output to the test.log, test_error.log file and terminal.
Automatic output is greater than the error information to the 'test_error.log' files.
![console](docs/async_output.png)
