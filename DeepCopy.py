from copy import copy, deepcopy
"""
deepcopy: 深拷贝，petter1是通过深拷贝创建的，我们对petter1对象添加宠物，不会影响petter对象。
copy: 浅拷贝，petter2是通过浅拷贝的方式创建的，我们对petter2对象增加宠物时，petter对象也跟着改变。

加粗：：
    浅拷贝拷贝引用类型对象的指针（指向），而不拷贝引用类型对象指向的值
    深拷贝则同时拷贝引用类型对象及其指向的值

引用类型：对象本身可以修改，Python中的引用类型有列表List，字典dictionary，类对象。Python在赋值的时候默认时浅拷贝。

使用克隆模式时，尽量使用深拷贝的方式（安全模式）
"""

class PetStore:
    def __init__(self, name) -> None:
        self.__name = name
        self.__petList = []

    def setName(self, name):
        self.__name = name

    def showMyself(self):
        print("%s 宠物店有以下宠物：" % self.__name)
        for pet in self.__petList:
            print(pet + "\t", end="")
        print()

    def addPet(self, pet):
        self.__petList.append(pet)


def testPetStore():
    petter = PetStore("Petter")
    petter.addPet("小狗Coco")
    print("父本petter：", end="")
    petter.showMyself()
    print()

    petter1 = deepcopy(petter)
    petter1.addPet("小猫Amy")
    print("副本petter1：", end="")
    petter1.showMyself()
    print("父本petter：", end="")
    petter.showMyself()
    print()

    petter2 = copy(petter)
    petter2.addPet("小兔Ricky")
    print("副本petter2：", end="")
    petter2.showMyself()
    print("父本petter：", end="")
    petter.showMyself()

# 父本petter：Petter 宠物店有以下宠物：
# 小狗Coco

# 副本petter1：Petter 宠物店有以下宠物：
# 小狗Coco        小猫Amy
# 父本petter：Petter 宠物店有以下宠物：
# 小狗Coco

# 副本petter2：Petter 宠物店有以下宠物：
# 小狗Coco        小兔Ricky
# 父本petter：Petter 宠物店有以下宠物：
# 小狗Coco        小兔Ricky


if __name__ == "__main__":
    testPetStore()
