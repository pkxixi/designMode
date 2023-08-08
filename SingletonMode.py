"""
单例模式：确保一个类只有一个实例，并且提供一个访问它的全局方法
# 设计思想：
    保证一个类只有一个对象（实例）的一种机制
"""


# 方式一：重写__new__ 和 __init__ 方法
# __new__ 是我们通过类名进行实例化对象时自动调用的，__init__是在每一次实例化对象之后调用的，
# __new__ 方法创建一个实例之后返回这个实例的对象，并将其传递给__init__方法的self参数
class Singleton:
    __instance = None
    __isFirstInit = False

    # __new__负责创建对象，是一个类方法
    def __new__(cls, name):
        if not cls.__instance:
            Singleton.__instance = super().__new__(cls)
        return cls.__instance

    # __init__负责初始化对象，是一个对象方法
    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            Singleton.__isFirstInit = True

    def getName(self):
        return self.__name


# 方式二：自定义metaclass的方法
class Singleton2(type):
    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None  # 初始化全局变量cls._instance为None

    def __call__(cls, *args, **kwargs):
        # 控制对象的创建过程，如果cls._instance为None，则创建；否则直接返回
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class CustomClass(metaclass=Singleton2):
    def __init__(self, name) -> None:
        self.name = name

    def getName(self):
        return self.name


def testSingleton():
    # tony = Singleton("tony")
    # karry = Singleton("karry")
    # print(tony.getName(), karry.getName())
    # print(id(tony), "-:-", id(karry))
    # print("tony==karry:", tony == karry)
    # ------------------
    tony = CustomClass("tony")
    karry = CustomClass("karry")
    print(tony.getName(), karry.getName())
    print(id(tony), "-:-", id(karry))
    print("tony==karry:", tony == karry)

if __name__ == "__main__":
    testSingleton()
