import os
import time
import subprocess


class AdbBase:
    def __init__(self, dev):
        self.dev = dev

    # 根据坐标点击228 174  1000 28
    def AdbShellInputTap(self, x, y):
        os.system("adb -s %s shell input tap %s %s" % (self.dev, x, y))

    # 输入字符
    def AdbShellInputText(self, text):
        os.system("adb -s %s shell input text %s" % (self.dev, text))

    # 等待时间
    def TimeSleepDuration(self, x):
        time.sleep(x)

    # 保存截图到指定路径
    def AdbShellScreencapPullRm(self, path):
        os.system("adb -s %s shell screencap -p /sdcard/screen.png" % self.dev)
        os.system("adb -s %s pull /sdcard/screen.png %s" % (self.dev, path))

    # //查看手机上第三方应用的packageName
    # //adb shell pm list packages -3
    def AdbShellPmListPackages(self):
        data = subprocess.Popen("adb -s %s shell pm list packages -3" % self.dev, shell=True, stdout=subprocess.PIPE,
                                encoding='utf-8')
        return data.stdout.read()

    def Adbdump(self,path):
        os.system("adb -s %s shell uiautomator dump --compressed /sdcard/window_dump.xml" % self.dev)
        os.system("adb -s %s pull /sdcard/window_dump.xml %s" % (self.dev, path))

# 测试点击
# Adb_base("127.0.0.1:7555").AdbShellInputTap(228, 174)
# time.sleep(1)
# Adb_base("127.0.0.1:7555").AdbShellInputTap(1000, 28)
# time.sleep(1)
# Adb_base("127.0.0.1:7555").AdbShellInputText("ssss")
# Adb_base("127.0.0.1:7555").AdbShellScreencapPullRm(r"D:\bao\1\0531落地页")
# print(Adb_base("127.0.0.1:7555").AdbShellPmListPackages())
AdbBase("127.0.0.1:7555").Adbdump(r"D:\bao\1\0531落地页")
