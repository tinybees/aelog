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

aelog.debug("simple debug message")
aelog.info("simple info message")
aelog.warning("simple warning message")
aelog.error("simple error message")
aelog.critical("simple critical message")
aelog.exception("simple exception message")
```
This will output to the terminal.
```

```

### To initialize, output log to file and terminal.
```
import aelog

aelog.init_aelog("test.log", True)

aelog.debug("simple debug message")
aelog.info("simple info message")
aelog.warning("simple warning message")
aelog.error("simple error message")
aelog.critical("simple critical message")
aelog.exception("simple exception message")
```
This will output to the test.log file and terminal.
```

```

### To initialize, asynchronous output log to file and terminal.
```
import asyncio
import aelog

aelog.init_aelog("test.log", True)

async def log_out():
    aelog.debug("simple debug message")
    aelog.info("simple info message")
    aelog.warning("simple warning message")
    aelog.error("simple error message")
    aelog.critical("simple critical message")
    aelog.exception("simple exception message")

if "__name__"=="__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(log_out())
```
This will output to the test.log file and terminal.
```

```

### 

# Todo
- Tests
