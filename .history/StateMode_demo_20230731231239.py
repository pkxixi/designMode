from abc import ABCMeta, abstractmethod


class Water:

    def __init__(self, state):
        self.__temperature = 25
        self.__state = state

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        if (self.__state):
            print("由", self.__state.getName(), "变为", state.getName())
        else:
            print("初始化为：", state.__getName())
        self.__state = state
    
    def getTemperature(self):
        return self.__temperature
    
    def setTemperature(self, temperature):
        if (self.__temperature <=)
