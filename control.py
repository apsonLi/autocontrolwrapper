import argparse
from adb import AdbBase
import os, time


class Control(object):
    """docstring for Control"""
    _emulatorList = {}

    def __init__(self, arg):
        super(Control, self).__init__()
        self.arg = arg
        self.path = r"E:\moniqi\Nox\bin"
        self.devices = {"1": "127.0.0.1:62025", "2": "127.0.0.1:62026", "3": "127.0.0.1:62027", "4": "127.0.0.1:62028"}

    def __run(self, cmd):
        execResult = os.popen(cmd)
        execResultStr = execResult.read()
        execResult.close()
        return execResultStr

    # 返回当前模拟器列表以及对应的状态
    def getEmulatorList(self):
        result = self.__run("adb devices").strip()
        for item in result.splitlines()[1:]:
            deviceName = item.split('device')[0].strip()
            adb = AdbBase(deviceName)
            self._emulatorList[deviceName] = adb.detectIsWorking()
        return self._emulatorList

    # 返回是否安装成功
    def getDeviceInstall(self, device, path):
        adb = AdbBase(device)
        result = adb.install_apk(path)
        return {"isInstallSuceess": result}

    # 启动模拟器多开，并自动连接adb
    def start_many(self, number):
        os.chdir(self.path)
        subprocess.Popen("NoxConsole.exe launch -name:夜神模拟器%s" % number, shell=True, stdout=subprocess.PIPE,
                         encoding='utf-8')
        time.sleep(20)
        for index, item in self.devices.items():
            if number == index:
                subprocess.Popen("adb connect %s" % item, shell=True, stdout=subprocess.PIPE,
                                 encoding='utf-8')

    # 关闭模拟器多开
    def stop_nox(self, number):
        os.chdir(self.path)
        subprocess.Popen("NoxConsole.exe quit -name:夜神模拟器%s" % number, shell=True, stdout=subprocess.PIPE,
                         encoding='utf-8')


parser = argparse.ArgumentParser(description="powered from apson")
parser.add_argument('-d', '--devicelist', help='返回')
parser.add_argument('-i', '--install', help='目标文件位置')

control = Control("")
args = parser.parse_args()
if args.devicelist:
    print(control.getEmulatorList())
if args.install:
    print(control.getDeviceInstall("3EP0219114001784", args.install))
