from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("着装：")


class Engineer(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

    def wear(self):
        print("我是 " + self.getSkill() + "工程师 " + self._name, end=", ")
        super().wear()


class Teacher(Person):

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def getTitle(self):
        return self.__title
    
    def wear(self):
        print("我是 " + self._name + self.getTitle(), end=", ")
        super().wear()

class ClothingDecorator(Person):
    """服装装饰器的基类"""
    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass

class CasualPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("这是一条卡其色休闲裤")

class LeatherShoesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("这是一双休闲皮鞋")


class BeltDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("这是一条银色针扣头的黑色腰带")
    

class KnittedSweaterDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("这是一件紫红色针织毛衣")

class WhiteShirtDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("这是一件白色衬衣")

class GlassesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("这是一副方形黑框眼镜")


def testDecorator():
    tony = Engineer("tony","客户端")
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweaterDecorator(shirt)
    glasses = GlassesDecorator(sweater)
    glasses.wear()

    print()
    decorateTeacher = GlassesDecorator(WhiteShirtDecorator(LeatherShoesDecorator(Teacher("wells","教授"))))
    decorateTeacher.wear()

if __name__ == "__main__":
    testDecorator()
