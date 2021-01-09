import os
import time
import subprocess

import wda

class idbBase:
    def __init__(self, dev, bundle_id = None, screenshot=None, pagesource=None):
        self.dev = wda.Client(dev)
        self.session = self.dev.session()
        self.bundle_id = bundle_id
        self.pagesource = pagesource
        self.screenshot = screenshot


    # 根据坐标点击228 174  1000 28
    def idbShellInputTap(self, x, y):
        self.session.tap(x,y)


    def idbShellInputText(self, text):
        pass
        # self.session.

    # 等待时间
    def TimeSleepDuration(self, x):
        time.sleep(x)

    # 保存截图到指定路径
    def idbShellScreencapPullRm(self, path):
        # if self.p is None:
        self.dev.screenshot(path)
        # 保存截图到指定路径

    # //查看手机上第三方应用的packageName
    # //idb shell pm list packages -3
    def idbShellPmListPackages(self):
        data = subprocess.Popen("ideviceinstaller -l")
        return data.stdout.read()

  

    # 根据字符，在dump文件中查找对应坐标 path:文件地址，不包括文件名，返回是：[[224.0, 174.5], [968.0, 468.5]]
    def idbDumpTap(self, target):
        bounds = self.session(text=target).get(timeout=2.0).bounds
        if bounds!=None:
            self.idbShellInputTap(bounds.x,bounds.y)





    # 启动apk
    def start_apk(self, bundle_id):
        self.session = self.dev.session(bundle_id)



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

    # 打印log到指定地址
    def log(self, info):
        if not self.f:
            return
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # print("%s" % i)
        tag = "idb[" + str(current_time) + "]:  "
        with open(self.f, 'a') as f:  # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
            f.write(str(tag) + str(info) + "\n")


def allStart():
    parser = argparse.ArgumentParser(description="powered from apson")
    parser.add_argument('-s', '--sid', help='输入设备id')
    parser.add_argument('-p', '--picturepath', help='图片地址')
    parser.add_argument('-apkPath', '---apkPath', help='apk路径')
    parser.add_argument('-w', '---windowpath', help='window.xml 路径')
    parser.add_argument('-d', '---debugfilepath', help='log文件路径')
    args = parser.parse_args()

    sid = args.sid
    picture = args.picturepath
    apkPath = args.apkPath
    windowpath = args.windowpath
    debugfilepath = args.debugfilepath

    idb = idbBase(sid, picture, windowpath, debugfilepath)
    ocr = OCRbase(picture)
    idb.log(10 * "-" + '初始化信息' + 10 * "-")

    idb.log("sid:" + sid)
    idb.log("picturepath:" + picture)
    idb.log("apkPath:" + apkPath)
    idb.log("windowpath:" + windowpath)
    return picture, apkPath, idb, ocr


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

idb = idbBase("http://localhost:8100")
idb.start_apk("com.tencent.xin")
idb.idbDumpTap("登录")
idb.killCurrentGame()
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
