import logging

logging.basicConfig(level=logging.INFO)


def loggingDecorator(func):
    def wrapperloggin(*args, **kwargs):
        logging.info("开始执行 %s() ..." % func.__name__)
        func(*args, **kwargs)
        logging.info("%s 执行完成！" % func.__name__)

    return wrapperloggin


def showInfo(*args, **kwargs):
    print("这是一个测试函数，参数：", args, kwargs)


decoratedShowInfo = loggingDecorator(showInfo)
decoratedShowInfo("arg1", "arg2", kwarg1=1, kwarg2=2)
