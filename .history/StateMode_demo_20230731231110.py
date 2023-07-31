from abc import ABCMeta, abstractmethod


class Water:

    def __init__(self, state):
        self.__temperature = 25
        self.__state = state

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        if (self.__state):
            print("由", self.__state.getName)