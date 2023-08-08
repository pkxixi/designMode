"""
克隆模式又叫原型模式
clone方法两个过程：
    - 分配一块新的内存空间给新的对象
    - 拷贝父本对象的属性

优缺点：
    + 克隆模式通过内存拷贝的方式进行复制，比new的方式创建对象性能更好
    + 通过深拷贝的方式，可以方便的创建一个具有相同属性和方法的另一个对象，特别是对于复杂对象，方便性尤为突出
    - 通过克隆模式创建对象，不会执行类的初始化函数(__init__())。这不一定是缺点，但大家使用的时候要注意这一点。
"""

from copy import copy, deepcopy

class Clone:

    def clone(self):
        # 浅拷贝模式克隆对象
        return copy(self)
    
    def deepClone(self):
        return deepcopy(self)