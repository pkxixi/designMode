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
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature()+step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature()-step)

    def behavior(self):
        state = self.getState()
        if isinstance(state, State):
            state.behavior(self)

    # 单例装饰器


def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton

# class State(metaclass=ABCMeta):

#     def __init__(self, name):
#         self.__name = name

#     def getName(self):
#         return self.__name

#     @abstractmethod
#     def behavior(self, water):
#         pass


@singleton
class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, water):
        print("我性格高冷，当前体温" + str(water.getTemperature())+"'C, 我坚如钢铁，仿如一冷血动物。")


@singleton
class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo > 0 and stateInfo < 100

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
