from abc import ABCMeta, abstractmethod
from enum import Enum


class DeviceType(Enum):
    """设备类型"""

    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3


class DeviceItem:
    """设备项"""

    def __init__(self, id, name, type, isDefault=False) -> None:
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault

    def __str__(self):
        return (
            "type: "
            + str(self.__type)
            + " id: "
            + str(self.__id)
            + " name: "
            + str(self.__name)
            + " isDefault: "
            + str(self.__isDefault)
        )

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def isDefault(self):
        return self.__isDefault


class DeviceList:
    """设备列表"""

    def __init__(self) -> None:
        self.__devices = []

    def add(self, deviceItem):
        self.__devices.append(deviceItem)

    def getCount(self):
        return len(self.__devices)

    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self.__devices[idx]

    def getById(self, id):
        for item in self.__devices:
            if item.getId() == id:
                return item
        return None


class DeviceMgr(metaclass=ABCMeta):
    @abstractmethod
    def enumerate(self):
        """枚举设备列表（在程序初始化时，有设备插拔时都要重新获取设备列表"""
        pass

    @abstractmethod
    def active(self, deviceId):
        """选择要使用的设备"""
        pass

    @abstractmethod
    def getCurDeviceId(self):
        pass


class SpeakerMgr(DeviceMgr):
    """扬声器设备列表"""

    def __init__(self) -> None:
        self.__curDeviceId = None

    def enumerate(self):
        """枚举设备列表，真实的项目应该通过驱动程序去读取设备信息，这里只用初始化来模拟"""
        devices = DeviceList()
        devices.add(
            DeviceItem(
                "21312dasd1", "Realtek High Definition Audio", DeviceType.TypeSpeaker
            )
        )
        devices.add(
            DeviceItem(
                "2219994832hdasd",
                "NVIDIA High Definition Audio",
                DeviceType.TypeSpeaker,
                True,
            )
        )
        return devices

    def active(self, deviceId):
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        return self.__curDeviceId


class DeviceUtil:
    def __init__(self) -> None:
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()

    def __getDeviceMgr(self, type):
        return self.__mgrs[type]

    def getDeviceList(self, type):
        return self.__getDeviceMgr(type).enumerate()

    def active(self, type, deviceId):
        self.__getDeviceMgr(type).active(deviceId)

    def getCurDeviceId(self, type):
        return self.__getDeviceMgr(type).getCurDeviceId()


def testDevices():
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print("外放设备列表：")
    if deviceList.getCount() > 0:
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())
    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)

    print(
        "当前使用的设备："
        + deviceList.getById(
            deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)
        ).getName()
    )


if __name__ == "__main__":
    testDevices()
