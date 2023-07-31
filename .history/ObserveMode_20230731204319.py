from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod(callable)