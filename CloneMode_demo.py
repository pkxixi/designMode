from copy import copy, deepcopy


class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def showMyself(self):
        print("我是" + self.__name + "，年龄是" + str(self.__age) + "。")

    def coding(self):
        print("我是码农，我用程序改变世界，coding······")

    def reading(self):
        print("阅读使我快乐！知识是我成长！如饥似渴地阅读时生活的一部分······")

    def fallInLove(self):
        print("春风吹，月亮明，花前月下好相约······")

    def clone(self):
        return copy(self)


def testClone():
    tony = Person("tony", 23)
    tony.showMyself()
    tony.coding()

    tony1 = tony.clone()
    tony1.showMyself()
    tony1.reading()

    tony2 = tony.clone()
    tony2.showMyself()
    tony2.fallInLove()


if __name__ == "__main__":
    testClone()