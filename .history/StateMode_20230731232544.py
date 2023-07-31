from abc import ABCMeta, abstractmethod

class Context(metaclass=ABCMeta):
    """状态模式的上下文环境"""

    def __init__(self):
        self.__states = []
        self.__curState = None
        # 状态发生
        self.__stateInfo = 0