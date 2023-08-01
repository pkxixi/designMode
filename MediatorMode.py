"""
中介模式又叫调停模式
# 设计思想：
    减少两个类的实际耦合
# 设计要点：
    1. 交互对象 interactiveObject: 要进行交互的一系列对象
    2. 中介者 mediator: 负责协调各个对象之间的交互
    3. 具体中介者 mediator: 中介的具体实现
# 优缺点：
    +  Mediator将原本分布于多个对象间的行为集中在一起，作为一个独立的概念并将其封装在一个对象中，简化了对象之间的交互
    +  将多个调用者与多个实现者之间多对多的交互关系，转换为一对多的交互关系，一对多的交互关系更易于理解，维护和扩展，大大减少了多个对象之间相互交叉引用的情况
    -  中介者承接了所有的交互逻辑，交互的复杂度转变成了中介者的复杂度，中介者类会变得越来越庞大和复杂，以至于后期可能会难以维护
    -  中介者出问题会导致多个使用者同时出现问题
# 应用场景：
    1. 一组对象以定义良好但复杂的方式进行通信，产生的相互依赖关系结构混乱且难以理解
    2. 一个对象引用其他很多对象并且直接与这些对象通信，导致难以复用该对象
    3. 想通过一个中间类来封装多个类中的行为，同时又不想生成太多的子类
"""


class InteractiveObject:
    """进行交互的对象"""
    pass

class InteractiveObjectImplA:
    """实现类A"""
    pass

class InteractiveObjectImplB:
    """实现类B"""
    pass

class Meditor:
    """中介类"""
    def __init__(self) -> None:
        self.__interactiveObjA = InteractiveObjectImplA()
        self.__interactiveObjB = InteractiveObjectImplB()
    
    def interactive(self):
        """进行交互的操作"""
        #通过self.__interactiveObjA 和self.__interactiveObjB完成响应的交互操作
        pass