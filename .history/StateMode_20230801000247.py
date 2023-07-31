from abc import ABCMeta, abstractmethod
"""
设计要点：
1. 实现状态模式的时候，实现的场景状态有时候会非常复杂，决定状态变化的因素也非常多，我们可以把决定状态变化的属性单独抽象成一个类StateInfo，
   这样判断状态属性是否符合当前的状态isMatch时就可以穿入更多的信息
2. 每一种状态应当只有唯一的实例
优缺点：
+  封装了状态的转换规则，在状态模式中可以将状态的转换代码封装在环境类中，对状态转换代码进行集中管理，而不是分散在一个个业务逻辑中
+  将所有与某个状态有关的行为放到一个类中，及状态类，使开发人员只专注于该状态下的逻辑开发
+  允许状态转换逻辑与状态对象合为一体，使用时只需要注入一个不同的状态对象即可使环境对象yong y
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