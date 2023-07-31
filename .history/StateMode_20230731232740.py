from abc import ABCMeta, abstractmethod

class Context(metaclass=ABCMeta):
    """状态模式的上下文环境"""

    def __init__(self):
        self.__states = []
        self.__curState = None
        # 状态发生变化依赖的属性，当者一个变量由多个变量共同决定时可以将其单独定义成一个类
        self.__stateInfo = 0
    
    def addState(self, state):
        if state not in self.__states:
            self.__states.append(state)
        
    def changeState(self, state):
        if state is None:
            return False
        if self.__curState is None:
            print("初始化为：")