import os
import time
import subprocess


# 根据坐标点击228 174  1000 28
def AdbShellInputTap(dev, x, y):
    os.system("adb -s %s shell input tap %s %s" % (dev, x, y))


# 输入字符
def AdbShellInputText(dev, text):
    os.system("adb -s %s shell input text %s" % (dev, text))


# 等待时间
def TimeSleepDuration(x):
    time.sleep(x)


# 保存截图到指定路径
def AdbShellScreencapPullRm(dev, path):
    os.system("adb -s %s shell screencap -p /sdcard/screen.png" % dev)
    os.system("adb -s %s pull /sdcard/screen.png %s" % (dev, path))


# //查看手机上第三方应用的packageName
# //adb shell pm list packages -3
def AdbShellPmListPackages(dev):
    data = subprocess.Popen("adb -s %s shell pm list packages -3" % dev, shell=True, stdout=subprocess.PIPE,
                            encoding='utf-8')
    return data.stdout.read()


# 测试点击
# AdbShellInputTap("127.0.0.1:7555", 228, 174)
# time.sleep(1)
# AdbShellInputTap("127.0.0.1:7555", 1000, 28)
# time.sleep(1)
# AdbShellInputText("127.0.0.1:7555", "ssss")
# AdbShellScreencapPullRm(r"D:\bao\1\0531落地页")
# print(AdbShellPmListPackages("127.0.0.1:7555"))
