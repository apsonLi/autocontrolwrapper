import os
import time
import subprocess

# 根据坐标点击228 174  1000 28
def AdbShellInputTap(x, y):
    os.system("adb shell input tap %s %s" % (x, y))


# 输入字符
def AdbShellInputText(text):
    os.system("adb shell input text %s" % text)


# 等待时间
def TimeSleepDuration(x):
    time.sleep(x)


# 保存截图到指定路径
def AdbShellScreencapPullRm(path):
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png %s" % path)


# //查看手机上第三方应用的packageName
# //adb shell pm list packages -3
def AdbShellPmListPackages():
    data = subprocess.Popen("adb shell pm list packages -3",shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return data.stdout.read()

# 测试点击
# AdbShellInputTap(228, 174)
# time.sleep(1)
# AdbShellInputTap(1000, 28)
# time.sleep(1)
# AdbShellInputText("ssss")
# AdbShellScreencapPullRm(r"D:\bao\1\0531落地页")
# print(AdbShellPmListPackages())