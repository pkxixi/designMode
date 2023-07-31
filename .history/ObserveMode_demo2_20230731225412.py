import time

class Account(Observable):
    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name":name, "ip":ip, "region":region, "time":time})
        self.__latestRegion[name]=region
        self.__latestIp[name]=ip
    
    def __getRegion(self, ip):
        # 由IP地址获得地区信息。这里只是模拟，真实项目中应该调用ip地址解析服务
        ipRegion