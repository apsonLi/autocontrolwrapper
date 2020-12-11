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

    def Adbdump(self, path):
        os.system("adb -s %s shell uiautomator dump --compressed /sdcard/window_dump.xml" % self.dev)
        os.system("adb -s %s pull /sdcard/window_dump.xml %s" % (self.dev, path))
        return os.path.join(path, "window_dump.xml")

    # 根据字符，在dump文件中查找对应坐标 path:文件地址，不包括文件名，返回是：[[224.0, 174.5], [968.0, 468.5]]
    def Adbdump_Tap(self, path, text):

        alltap = []
        file = self.Adbdump(path)
        json_data = self.xml_to_json(file)
        # print(json_data)
        for _, values in json_data.items():
            for _, value in values.items():
                if value != '0':
                    for key, data in value.items():
                        if key == "node":
                            for k in data:
                                for z in k:
                                    if z == "node":
                                        for i in k[z]:
                                            if type(i) is dict:
                                                for m, n in i.items():
                                                    if text == n:
                                                        all_value = i["@bounds"]
                                                        # print(all_value)
                                                        a = []
                                                        b = []
                                                        tap = []
                                                        for index, x in enumerate(re.findall('\d+', all_value)):
                                                            if index % 2 == 1:
                                                                b.append(int(x))
                                                            else:
                                                                a.append(int(x))
                                                        tap.append(sum(a) / 2.0)
                                                        tap.append(sum(b) / 2.0)
                                                        alltap.append(tap)

        return alltap


    # xml文件转换成json
    def xml_to_json(self, xml):
        xml_file = open(xml, "r", encoding="utf-8")
        xml_str = xml_file.read()
        xml_parse = xmltodict.parse(xml_str)
        json_str = json.dumps(xml_parse, ensure_ascii=False, indent=1)
        json_data = json.loads(json_str)
        return json_data


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
