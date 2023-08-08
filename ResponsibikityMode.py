"""
职责模式，又称责任链模式，它将请求的发送者和接收者解耦了。客户端不需要知道请求处理者的明确信息和处理的具体逻辑，甚至不需要知道链的结构，它只需要将请求发送即可

Requester是请求的发送者，是请求的包装类，封装一个请求对象。
Responsible是责任人的抽象基类，也是责任链的节点；
Responsible中有一个指向自身的引用，也就是下一个责任人，这是责任链形成的关键。

设计要点：
    · 请求者和请求内容：确认谁要发送请求，发送请求的对象成为请求者。请求的内容通过发送请求时的参数进行传递。
    · 有哪些责任人：责任人是构成责任链的关键要素。请求的流动方向是链条中的线，而责任人是链条上的节点。
    · 对责任人的抽象：责任人的共同特征是都可以处理请求，所以需要对责任人进行抽象，使他们具有责任的可传递性
    · 责任人可自由组合：责任链上的责任人可以巨根业务的具体逻辑进行自由的组合和排序
优缺点：
    + 降低耦合度。这种模式将请求的发送者和接收者解耦
    + 简化了对象。它使得对象不需要知道链的结构
    + 增强给对象指派职责的灵活性。可改变链内的成员或者调动他们的次序，允许动态地新增或删除责任人
    + 增加新的处理类很方便
    - 不能保证请求一定被处理
    - 系统性能将受到一定的影响，而且在进行代码调试时不太方便，可能会造成循环调用
应用场景：
    · 多个对象同时处理同一个请求，具体哪个对象处理该请求在运行时刻自动确定
    · 请求的处理有明显的一层层传递关系
    · 请求的处理流程和顺序需要程序运行时动态确定
    · 常见的审批流程（财务报销，转岗申请等）

"""

from abc import ABCMeta, abstractmethod


class Requester:
    def __init__(self, name, dayoff, reason) -> None:
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def getName(self):
        return self.__name

    def getDayOff(self):
        return self.__dayoff

    def getReason(self):
        return self.__reason

    def setLeader(self, leader):
        self.__leader = leader


class Responsible(metaclass=ABCMeta):
    def __init__(self, name, title) -> None:
        self.__name = name
        self.__title = title
        self._nextHandler = None

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.__title

    def getNextHandler(self):
        return self._nextHandler

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    def handleRequest(self, request):
        # 当前责任人处理请求
        self._handleRequestImpl(request)
        if self._nextHandler is not None:
            self._nextHandler.handleRequesImpl(request)

    @abstractmethod
    def handleRequestImpl(self, request):
        # 真正处理请求的方法
        pass
