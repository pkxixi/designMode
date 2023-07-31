from abc import ABCMeta, abstractmethod
from StateMode import Context

class Water(Context):

    def __init__(self):
        super.__init__()
        self.addState(SolidState("固态"))
        self.addState(SolidState("液态"))
        self.addState(SolidState("气态"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temp)

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
    water = Water(LiquidState("液态"))
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(20)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()


if __name__ == "__main__":
    testState()
