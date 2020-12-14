import os
import time
import subprocess
import xmltodict
import json
import re


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

    def __adbDump(self):
        path = os.getcwd()
        os.system("adb -s %s shell uiautomator dump --compressed /sdcard/window_dump.xml" % self.dev)
        os.system("adb -s %s pull /sdcard/window_dump.xml %s" % (self.dev, path))
        return os.path.join(path, "window_dump.xml")

    # 根据字符，在dump文件中查找对应坐标 path:文件地址，不包括文件名，返回是：[[224.0, 174.5], [968.0, 468.5]]
    def adbDumpTap(self, text):
        file = self.__adbDump()
        json_data = self.xml_to_json(file)
        self.__cyclefromNode(json_data["hierarchy"],text)

    def __cyclefromNode(self,json,text):
        #遍历每个Node节点
        if isinstance(json,dict) and 'node' in json.keys():
            self.__cyclefromNode(json['node'],text)
        elif isinstance(json,list) or isinstance(json,tuple):
            for item in json:
                self.__cyclefromNode(item,text)
        else:
            if text == json["@text"]:
                point = json["@bounds"].split('][')[0][1:].split(",")
                self.AdbShellInputTap(point[0],point[1])
                return True
            


    # xml文件转换成json
    def xml_to_json(self, xml):
        xml_file = open(xml, "r", encoding="utf-8")
        xml_str = xml_file.read()
        xml_parse = xmltodict.parse(xml_str)
        json_str = json.dumps(xml_parse, ensure_ascii=False, indent=1)
        json_data = json.loads(json_str)
        return json_data

    # 返回packageName 和 launcher_act
    def getAPKInfo(self, filePath):
        data = os.popen("aapt dump badging %s | findstr package" % filePath).read()
        apkname = data.split('\'')[1]

        data3 = subprocess.Popen("aapt dump badging %s | findstr launchable-activity" % filePath,
                                 shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        launchable_activity = data3.stdout.read().split('\'')[1]

        return apkname, launchable_activity

    # 安装apk
    def install_apk(self, path):
        result = subprocess.Popen("adb -s %s install %s" % (self.dev, path),
                                 shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout.read()
        if 'Success' in result:
            return True
        else:
            return False

    # 卸载apk
    def uninstall_apk(self, path):
        apkname, _ = self.getAPKInfo(path)
        os.system("adb -s %s uninstall %s" % (self.dev, apkname))

    # 启动apk
    def start_apk(self, path):
        apkname, activity = self.getAPKInfo(path)
        os.system("adb -s {0} shell am start -n {1}/{2}".format(self.dev, apkname, activity))

    #判断是否存在包名
    def findIsExitPackage(self,path):
        apkname, _ = self.getAPKInfo(path)
        data = self.AdbShellPmListPackages()
        for i in data:
            if apkname in i:
                return True
            else:
                return False


    #判断模拟器是否在运行中
    def detectIsWorking(self):
        result = subprocess.Popen("adb shell dumpsys activity | grep mResumedActivity" ,
                                 shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        result = result.stdout.read()
        if result != None and 'com.vphone.launcher/.Launcher' in  result:
            return False
        else:
            return True

    # 关闭当前应用
    def killCurrentGame(self,apkname):
        os.system("adb -s %s shell am force-stop %s" % (self.dev, apkname))




# 测试点击
# Adb_base("127.0.0.1:7555").AdbShellInputTap(228, 174)
# time.sleep(1)
# Adb_base("127.0.0.1:7555").AdbShellInputTap(1000, 28)
# time.sleep(1)
# Adb_base("127.0.0.1:7555").AdbShellInputText("ssss")
# Adb_base("127.0.0.1:7555").AdbShellScreencapPullRm(r"D:\bao\1\0531落地页")
# print(Adb_base("127.0.0.1:7555").AdbShellPmListPackages())
# print(AdbBase("127.0.0.1:7555").Adbdump(r"D:\bao\1\0531落地页"))
# print(AdbBase("127.0.0.1:7555").xml_to_json(r"D:\bao\1\0531落地页\window_dump.xml"))
# print(AdbBase("127.0.0.1:7555").Adbdump_Tap(r"D:\bao\1\0531落地页", "微信"))
a= AdbBase("3EP0219114001784")
print(a.adbDumpTap("知乎"))
# a= AdbBase("127.0.0.1:62001").install_apk(r"D:\bao\apk\20201130\222.apk")

# print(a)

# AdbBase("127.0.0.1:62027").install_apk(r"D:\bao\apk\20201130\222.apk")
