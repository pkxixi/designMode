from abc import ABCMeta, abstractmethod


class Person:
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

    def request(self):
        print("%s 申请请假 %d 天，请假事由：%s" % (self.__name, self.__dayoff, self.__reason))
        if self.__leader is not None:
            self.__leader.handleRequest(self)


class Manager(metaclass=ABCMeta):
    def __init__(self, name, title) -> None:
        self.__name = name
        self.__title = title
        self._nextHandler = None

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.__title

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    @abstractmethod
    def handleRequest(self, person):
        pass


class Supervisor(Manager):
    def __init__(self, name, title) -> None:
        super().__init__(name, title)

    def handleRequest(self, person):
        if person.getDayOff() <= 2:
            print(
                "同意 %s 请假，签字人 %s(%s)"
                % (person.getName(), self.getName(), self.getTitle())
            )
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class DepartmentManager(Manager):
    def __init__(self, name, title) -> None:
        super().__init__(name, title)

    def handleRequest(self, person):
        if person.getDayOff() > 2 and person.getDayOff() <= 5:
            print(
                "同意 %s 请假，签字人 %s(%s)"
                % (person.getName(), self.getName(), self.getTitle())
            )
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class CEO(Manager):
    def __init__(self, name, title) -> None:
        super().__init__(name, title)

    def handleRequest(self, person):
        if person.getDayOff() > 5 and person.getDayOff() <= 22:
            print(
                "同意 %s 请假，签字人 %s(%s)"
                % (person.getName(), self.getName(), self.getTitle())
            )
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class Administrator(Manager):
    def __init__(self, name, title) -> None:
        super().__init__(name, title)

    def handleRequest(self, person):
        print("%s 的请假申请已审核，情况属实！已备案处理，处理人：%s(%s)\n" % (person.getName(), self.getName(), self.getTitle()))


def testAskForLeave():
    directLeader = Supervisor("Eren", "客户端研发部经理")
    departmentLeader = DepartmentManager("Eric", "技术研发中心总监")
    ceo = CEO("Helen", "创新文化公司CEO")
    administrator = Administrator("Nina", "行政中心总监")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    sunny = Person("sunny", 1, "参加MDCC大会。")
    sunny.setLeader(directLeader)
    sunny.request()

    tony = Person("tony", 5, "家里有紧急事情！")
    tony.setLeader(directLeader)
    tony.request()

    pony = Person("pony", 15,"出国深造。")
    pony.setLeader(directLeader)
    pony.request()

if __name__ == "__main__":
    testAskForLeave()