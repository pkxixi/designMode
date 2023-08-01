"""
装饰器模式，动态的给对象增加一些额外的职责，就扩展对象功能来说，装饰模式比生成子类的方式更加灵活
python中的装饰器：
    包装一个函数，并改变（扩展）它的行为
    装饰器可以是一个类（类中必须实现__call__方法，使其是callable的），也可以是一个函数。装饰器不仅可以修改一个函数，还可以修饰一个类。如下示例：
# 设计要点：
1. 可灵活地给一个对象增加职责或扩展功能
2. 可增加任一多个装饰
3. 装饰的顺序不同，可能产生的效果不同
# 优缺点：
+. 使用装饰模式来实现扩展比使用继承更加灵活，它可以在不创造更多的子类的情况下，将对象的功能加以扩展
+. 可以动态地给一个对象附加更多的功能
+. 可以用不同的装饰器进行多重装饰，装饰的顺序不同，可能产生不同的效果
+. 装饰类和被装饰类可以独立发展，不会相互耦合，装饰模式相当于继承一个替代模式
-. 和继承相比，用装饰的方式扩展功能容易出错，排错也更困难。对于多次装饰的对象，调试寻找错误时可能需要逐级排查，较为繁琐

# 应用场景：
1. 大量独立的扩展，为支持每一种组合将产生大量的子类，使得子类数目呈爆炸性增长时
2. 需要动态地增加或撤销功能时
3. 不能采用生成子类的方法进行扩充时，类的定义不能用于生成子类（如Java中的final类）
"""


# decorator class
class ClassDecorator:
    def __init__(self, func) -> None:
        self.__numofCall = 0
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__numofCall += 1
        obj = self.__func(*args, **kwargs)
        print("创建%s的第%d个实例：%s" % (self.__func.__name__, self.__numofCall, id(obj)))
        return obj


@ClassDecorator
class Myclass:
    def __init__(self, name) -> None:
        self.__name = name

    def getName(self):
        return self.__name
    
tony = Myclass("tony")
karry = Myclass("karry")
print(id(tony))
print(id(karry))

