from abc import ABCMeta, abstractmethod
"""
监听模式又叫观察者模式，是对象的行为模式，又叫发布/订阅模式，模型/视图模式，源/监听模式，或者从属者（dependents）模式
"""
# 1. 明确谁是观察者，谁是被观察者，是多对一的关系。
# 2. Observalbe 在发送广播通知的时候，无须指定具体的observer， observer可以自己决定是否订阅通知
# 3. 被观察者至少有三个方法：添加监听者，删除监听者，通知observer的方法。观察者至少有一个方法：更新方法，及更新当前的内容，做出相应的处理

# 应用场景：
# 1. 对一个对象状态
class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)