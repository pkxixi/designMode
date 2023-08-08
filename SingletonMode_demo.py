class MyBeautifulGril:
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGril.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇见"+name+"。我一见钟情！")
            MyBeautifulGril.__isFirstInit = True
        else:
            print("遇见"+name+"。我置若罔闻!")

    def showMyHeart(self):
        print(self.__name+"就是我心中的唯一！")

def testLove():
    jenny = MyBeautifulGril("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGril("Kimi")
    kimi .showMyHeart()
    print("id(Jenny):", id(jenny)," id(Kimi):",id(kimi))

if __name__=="__main__":
    testLove()