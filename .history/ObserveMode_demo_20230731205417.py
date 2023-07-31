class WaterHeater(Observable):
    
    def __init__(self):
        super.__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是："+str(self.__temperature)+"'C")
        self.notifyObservers()
    
class WashingMode(observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature()<70:
            print("shui")