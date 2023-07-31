class WaterHeater(Observable):
    
    def __init__(self):
        super.__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是："+str()) 