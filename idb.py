import os
import time
import subprocess
import argparse
import wda
import json


class idbBase:
    def __init__(self, dev, bundle_id=None, screenshot=None, debugfilepath=None, log=None):
        print(dev)
        print(bundle_id)
        self.dev = wda.Client(dev)
        self.session = self.dev.session()
        self.bundle_id = bundle_id
        self.screenshot = screenshot
        self.debugfilepath = debugfilepath
        self.detaillog = log

    # 根据坐标点击228 174  1000 28
    def idbShellInputTap(self, state, x, y):
        self.printLog(state, "点击位置:" + str(x) + "|" + str(y))
        self.session.tap(x, y)

    def idbShellInputText(self, text):
        pass
        # self.session.

    # 等待时间
    def TimeSleepDuration(self, x):
        time.sleep(x)

    # 保存截图到指定路径
    def idbShellScreencapPullRm(self, path):
        self.printLog("截取截图", "截取图片%s" % path)
        if self.screenshot is None:
            self.dev.screenshot(path)
        else:
            self.dev.screenshot(self.screenshot)
        self.printLog("截取截图", "截取图片%s完成" % path)
        # 保存截图到指定路径

    # //查看手机上第三方应用的packageName
    # //idb shell pm list packages -3
    def idbShellPmListPackages(self):
        data = subprocess.Popen("ideviceinstaller -l")
        return data.stdout.read()

    # 根据字符，在dump文件中查找对应坐标 path:文件地址，不包括文件名，返回是：[[224.0, 174.5], [968.0, 468.5]]
    def idbDumpTap(self, state, target):
        bounds = self.session(text=target).get(timeout=2.0).bounds
        if bounds != None:
            self.idbShellInputTap(state, bounds.x, bounds.y)

    def idbDumpTap2(self, state, target):
        self.printLog(state, "点击%s" % target)
        self.session(text=target).click_exists(timeout=8.0)

    def idbDump(self):
        result = self.dev.source(accessible=True)
        print(result)

    # 启动apk
    def start_apk(self, bundle_id):
        self.printLog("启动app", "启动app %s" % bundle_id)
        if self.bundle_id is not None:
            self.session = self.dev.session(self.bundle_id)
        else:
            self.session = self.dev.session()
        self.printLog("启动app", "启动app成功")

    def gotosafir(self):
        self.session = self.dev.session('com.apple.mobilesafari', ['-u', 'https://apps.apple.com/cn/app/id1542975286'])
        print(self.session.orientation)
        # s.close()

    # 判断模拟器是否在运行中
    def detectIsWorking(self):
        result = self.dev.app_current()
        if result != None and 'com.apple.springboard' == result:
            return False
        else:
            return True

    # 关闭当前应用
    def killCurrentGame(self):
        self.session.close()
        self.printLog("关闭应用", "关闭应用%s" % self.bundle_id)

    # 打印log到指定地址
    def log(self, info):
        if not self.debugfilepath:
            return
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # print("%s" % i)
        tag = "idb[" + str(current_time) + "]:  "
        with open(self.debugfilepath, 'a') as f:  # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
            f.write(str(tag) + str(info) + "\n")

    def printLog(self, state, info):
        if not self.detaillog:
            return
        else:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            value = {"time": current_time, "level": "info", "stage": state, "msg": info}
            print(json.dumps(value))


def allStart():
    parser = argparse.ArgumentParser(description="powered from apson")
    parser.add_argument('-s', '--sid', help='输入设备id')
    parser.add_argument('-p', '--picturepath', help='图片地址')
    parser.add_argument('-b', '--bundle_id', help='bundle_id')
    parser.add_argument('-d', '---debugfilepath', help='log文件路径')
    parser.add_argument('-l', '---detaillog', help='是否需要输出日志')
    args = parser.parse_args()

    sid = args.sid
    # sid = "http://172.16.2.151:9527"
    picture = args.picturepath
    bundle_id = args.bundle_id
    bundle_id2 = "com.xmcyu.vbgfe"
    debugfilepath = args.debugfilepath
    log = args.detaillog

    idb = idbBase(sid, bundle_id2, picture, debugfilepath, log)
    idb.log(10 * "-" + '初始化信息' + 10 * "-")
    idb.log("sid:" + sid)
    idb.log("bundle_id:" + bundle_id)
    idb.log("picture:" + picture)
    return picture, idb


def dataRe(state=0, err="", datas=""):
    if state == 1 or state is None:
        value = {
            "state": state,
            "data": {
                "districtName": "",
            },
            "err": err
        }
    else:
        value = {
            "state": state,
            "data": {
                "districtName": datas,
            },
            "err": ""
        }
    return value

# 测试点击
# idbBase("127.0.0.1:62001").idbShellInputTap(1036, 225)
# time.sleep(1)
# idb_base("127.0.0.1:7555").idbShellInputTap(1000, 28)
# time.sleep(1)
# idb_base("127.0.0.1:7555").idbShellInputText("ssss")
# idbBase("127.0.0.1:62001").idbShellScreencapPullRm(r"D:\bao\1\0531落地页")
# print(idb_base("127.0.0.1:7555").idbShellPmListPackages())
# print(idbBase("127.0.0.1:7555").idbdump(r"D:\bao\1\0531落地页"))
# print(idbBase("127.0.0.1:7555").xml_to_json(r"D:\bao\1\0531落地页\window_dump.xml"))
# print(idbBase("127.0.0.1:7555").idbdump_Tap(r"D:\bao\1\0531落地页", "微信"))
# a = idbBase("127.0.0.1:62001")
# a.idbDumpTap("游客登录")
# a= idbBase("127.0.0.1:62001").install_apk(r"D:\bao\apk\20201130\222.apk")

# print(a)

# idbBase("127.0.0.1:62027").install_apk(r"D:\bao\apk\20201130\222.apk")
