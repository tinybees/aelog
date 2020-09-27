## Aelog Changelog

###[1.0.6] - 2020-9-27

#### Added
- 新增sanic日志格式以支持sanic的access日志输出
- 增加类型标注
- 删除废弃的功能

###[1.0.6] - 2020-8-30

#### Added
- 新增输出日志的级别开关功能
- 新增console输出也能增加日志级别的功能

#### Changed
- 修复文件中输出的日志无法输出debug日志的情况


###[1.0.5] - 2020-6-27

#### Changed
- 修复如果打印的log参数不是字符串会报错的问题

###[1.0.4] - 2020-6-14

#### Added 
- 增加日志中可以直接输入多个参数的功能,除了exception级别的日志.

#### Changed
- 优化各个级别的日志中影响性能的判断逻辑.
- 删除已经废弃,不再支持的功能.
- 修改最低支持的Python版本为3.6版本.

###[1.0.3] - 2018-12-23

#### Added 

- 增加init_app初始化方法，可以直接传入app初始化（参考类flask扩展的方式）
- 增加指定错误日志文件的功能，如没有指定则和老版本处理方式相同

#### Changed
- 修改init_aelog实现方式，增加警告内容
- 增加log文件的校验，保证是log结尾的日志文件
- 重构部分内容

###[1.0.1] - 2018-03-28

#### Added 

- 测试完成，发布到pypi


#### Changed
- 修改直接在终端执行报错的问题

###[1.0.0] - 2018-03-25

#### Added 

- Make using python log as simple as possible.
- Output log contains the full package name path.
- Provide asynchronous log output function, at the same time, contains common log output.
- Output according to the log level to mark the different colors separately.
- Provide a log rotating, automatic backup.
- Default output to the terminal, if you don't provide the log file path.
- Edit readme,push to pypi, and so on.


#### Changed
