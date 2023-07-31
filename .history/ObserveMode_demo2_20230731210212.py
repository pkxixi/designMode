import time

class Account(Observable):
    def __init__(self):
        super().__init__()
        self.__latestIp = {}