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
        if (self.__temperature <= 0):
            self.changeState(SolidState("固态"))
        elif self.__temperature <= 100:
            self.changeState(LiquidState("液态"))
        else:
            self.changeState(GaseousState("气态"))

    def riseTemperature(self, step):
        self.setTemperature(self.__temperature+step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature-step)

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def behavior(self, water):
        pass


class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格高冷，当前体温" + str(water.getTemperature())+"'C, 我坚如钢铁，仿如一冷血动物。")


class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格温和，当前体温" + str(water.getTemperature())+"'C, 我可温润万物。")


class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格热烈，当前体温" + str(water.getTemperature())+"'C, 飞向天空是我毕生的梦想。")


def testState():
    