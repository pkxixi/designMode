from abc import ABCMeta, abstractmethod
"""
设计要点：
1. 实现状态模式的时候，实现的场景状态有时候会非常复杂，决定状态变化的因素也非常多，我们可以把决定状态变化的属性单独抽象成一个类StateInfo
"""

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
            print("初始化为：", state.getName())
        else:
            print("由", self.__curState.getName(), "变为", state.getName())

        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState
    
    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if state.isMatch(stateInfo):
                self.changeState(state)
    
    def _getStateInfo(self):
        return self.__stateInfo


class State:
    """抽象状态类，负责状态的定义和接口的统一，StateA和StateB是具体的状态类，如水的三种状态。context是上下文环境类，负责具体状态的切换"""
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def isMatch(self, stateInfo):
        """状态的属性stateInfo是否在当前的状态范围内"""
        return True

    def behavior(self, context):
        pass