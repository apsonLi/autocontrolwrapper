from ocr import OCRbase
import time
import adb
import json

picture, apkPath, devices, ocr = adb.allStart()
name, _ = devices.getAPKInfo(apkPath)


# 判断我在江湖公告
def is_notice(data):
    n = 0
    while n < 3:
        if "请查看大图" in data or "区" not in data:
            time.sleep(2)
            devices.AdbShellInputTap("关闭公告重试", 1361, 89)
            time.sleep(2)
            devices.AdbShellScreencapPullRm(picture)
            time.sleep(2)
            qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
            time.sleep(2)
            data = qfvalue.ocr_QFdata()
            n += 1
        else:
            break
    return data


# 判断其他公告
def is_notice_other(data):
    n = 0
    while n < 3:
        if "请查看大图" in data or "国" not in data:
            time.sleep(2)
            devices.AdbShellInputTap("关闭公告重试", 1327, 94)
            time.sleep(2)
            devices.AdbShellScreencapPullRm(picture)
            time.sleep(2)
            qfvalue = OCRbase(picture, isFix=True, topX=1007, bottomX=1333, topY=447, bottomY=503)
            time.sleep(2)
            data = qfvalue.ocr_QFdata()
            n += 1
        else:
            break
    return data


# 判断山海经公告
def is_notice_shj(data):
    n = 0
    while n < 3:
        if "请查看大图" in data or "服" not in data:
            time.sleep(2)
            devices.AdbShellInputTap("关闭公告重试", 1, 1)
            time.sleep(2)
            devices.AdbShellScreencapPullRm(picture)
            time.sleep(2)
            qfvalue = OCRbase(picture, isFix=True, topX=330, bottomX=580, topY=1150, bottomY=1190)
            time.sleep(2)
            data = qfvalue.ocr_QFdata()
            n += 1
        else:
            break
    return data


# 判断九州行公告
def is_notice_jzx(data):
    n = 0
    while n < 3:
        if "请查看大图" in data or "服" not in data:
            time.sleep(2)
            devices.AdbShellInputTap("关闭公告重试", 944, 673)
            time.sleep(2)
            devices.AdbShellScreencapPullRm(picture)
            time.sleep(2)
            qfvalue = OCRbase(picture, isFix=True, topX=592, bottomX=841, topY=516, bottomY=564)
            time.sleep(2)
            data = qfvalue.ocr_QFdata()
            n += 1
        else:
            break
    return data


# 判断青云传2公告
def is_notice_qyz2(data):
    n = 0
    while n < 3:
        if "请查看大图" in data or "服" not in data:
            time.sleep(2)
            devices.AdbShellInputTap("关闭公告重试", 1022, 730)
            time.sleep(2)
            devices.AdbShellScreencapPullRm(picture)
            time.sleep(2)
            qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=826, topY=504, bottomY=561)
            time.sleep(2)
            data = qfvalue.ocr_QFdata()
            n += 1
        else:
            break
    return data


# 判断青云传公告
def is_notice_qyz3(data):
    n = 0
    while n < 3:
        if "请查看大图" in data or "服" not in data:
            time.sleep(2)
            devices.AdbShellInputTap("关闭公告重试", 898, 735)
            time.sleep(2)
            devices.AdbShellScreencapPullRm(picture)
            time.sleep(2)
            qfvalue = OCRbase(picture, isFix=True, topX=604, bottomX=880, topY=504, bottomY=590)
            time.sleep(2)
            data = qfvalue.ocr_QFdata()
            n += 1
        else:
            break
    return data


# 判断苍穹公告
def is_notice_cq(data):
    n = 0
    while n < 3:
        if "请查看大图" in data or "服" not in data:
            time.sleep(2)
            devices.AdbShellInputTap("关闭公告重试", 1454, 97)
            time.sleep(2)
            devices.AdbShellScreencapPullRm(picture)
            time.sleep(2)
            qfvalue = OCRbase(picture, isFix=True, topX=569, bottomX=818, topY=555, bottomY=615)
            time.sleep(2)
            data = qfvalue.ocr_QFdata()
            n += 1
        else:
            break
    return data


def rule():
    # 遮天
    # devices.start_apk(apkPath)
    # time.sleep(100)
    # devices.AdbShellInputTap("点击用户协议", 528, 589)
    # time.sleep(2)
    # devices.adbDumpTap("游客登录", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭手机绑定", 1080, 225)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭福利", 1154, 168)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1154, 168)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(2)
    # data = qfvalue.ocr_QFdata()
    # if "正在" in data:
    #     time.sleep(2)
    #     devices.AdbShellInputTap("点击进入游戏", 777, 668)
    #     time.sleep(2)
    #     devices.AdbShellInputTap("点击用户协议", 528, 589)
    #     time.sleep(2)
    #     devices.adbDumpTap("游客登录", apkPath)
    #     time.sleep(5)
    #     devices.AdbShellInputTap("关闭手机绑定", 1080, 225)
    #     time.sleep(2)
    #     devices.AdbShellInputTap("关闭福利", 1154, 168)
    #     time.sleep(2)
    #     devices.AdbShellInputTap("关闭公告", 1361, 89)
    #     time.sleep(2)
    #     devices.AdbShellInputTap("关闭公告", 1154, 168)
    #     time.sleep(2)
    #     devices.AdbShellScreencapPullRm(picture)
    #     time.sleep(2)
    #     qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    #     time.sleep(2)
    #     data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 疯狂走位
    # devices.start_apk(apkPath)
    # time.sleep(100)
    # devices.adbDumpTap("快速游戏", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 反向操作
    # devices.start_apk(apkPath)
    # time.sleep(100)
    # devices.adbDumpTap("用户注册", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1327, 94)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=1007, bottomX=1333, topY=447, bottomY=503)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_other(data)

    # 憨憨大作战
    # devices.start_apk(apkPath)
    # time.sleep(15)
    # devices.AdbShellInputTap("关闭启动公告", 636, 701)
    # time.sleep(100)
    # devices.AdbShellInputTap("点击用户协议", 558, 706)
    # time.sleep(2)
    # devices.adbDumpTap("帐号登录", apkPath)
    # time.sleep(2)
    # # devices.adbDumpTap("使用其他方式登录", apkPath)
    # # time.sleep(2)
    # devices.AdbShellInputText("15207676214")
    # time.sleep(2)
    # devices.AdbShellInputTap("点击输入密码", 658, 436)
    # time.sleep(2)
    # devices.AdbShellInputText("123456")
    # time.sleep(2)
    # devices.adbDumpTap("进入游戏", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 地下城勇者
    # devices.start_apk(apkPath)
    # time.sleep(15)
    # devices.AdbShellInputTap("关闭启动公告", 636, 701)
    # time.sleep(100)
    # devices.AdbShellInputTap("点击用户协议", 558, 706)
    # time.sleep(2)
    # devices.adbDumpTap("帐号登录", apkPath)
    # time.sleep(2)
    # # devices.adbDumpTap("使用其他方式登录", apkPath)
    # # time.sleep(2)
    # devices.AdbShellInputText("15207676214")
    # time.sleep(2)
    # devices.AdbShellInputTap("点击输入密码", 658, 436)
    # time.sleep(2)
    # devices.AdbShellInputText("123456")
    # time.sleep(2)
    # devices.adbDumpTap("进入游戏", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 山海经吞噬
    # devices.start_apk(apkPath)
    # time.sleep(30)
    # devices.adbDumpTap("进入游戏", apkPath)
    # time.sleep(10)
    # devices.adbDumpTap("返回", apkPath)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1, 1)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # qfvalue = OCRbase(picture, isFix=True, topX=330, bottomX=580, topY=1150, bottomY=1190)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_shj(data)

    # 逆天魔童
    # devices.start_apk(apkPath)
    # time.sleep(60)
    # devices.adbDumpTap("快速注册", apkPath)
    # time.sleep(2)
    # devices.adbDumpTap("进入游戏", apkPath)
    # time.sleep(5)
    # devices.adbDumpTap("稍后填写", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 944, 673)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # qfvalue = OCRbase(picture, isFix=True, topX=592, bottomX=841, topY=516, bottomY=564)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_jzx(data)

    # 上古仙缘
    # devices.start_apk(apkPath)
    # time.sleep(100)
    # devices.adbDumpTap("游客登录", apkPath)
    # time.sleep(5)
    # devices.adbDumpTap("确定", apkPath)
    # time.sleep(2)
    # devices.adbDumpTap("登录", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭福利", 1117, 190)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭实名", 492, 176)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭福利", 1117, 190)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1022, 730)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=826, topY=504, bottomY=561)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_qyz2(data)

    # 三生枕上书：三世情缘
    # devices.start_apk(apkPath)
    # time.sleep(50)
    # devices.AdbShellInputTap("点击更新", 808, 619)
    # time.sleep(60)
    # devices.adbDumpTap("游客登录", apkPath)
    # time.sleep(5)
    # devices.adbDumpTap("确定", apkPath)
    # time.sleep(2)
    # devices.adbDumpTap("登录", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭实名", 492, 176)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 898, 735)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # qfvalue = OCRbase(picture, isFix=True, topX=604, bottomX=880, topY=504, bottomY=590)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_qyz3(data)

    # 青狐传说
    # devices.start_apk(apkPath)
    # time.sleep(100)
    # devices.adbDumpTap("游客登录", apkPath)
    # time.sleep(5)
    # devices.adbDumpTap("确定", apkPath)
    # time.sleep(2)
    # devices.adbDumpTap("登录", apkPath)
    # # time.sleep(5)
    # devices.AdbShellInputTap("关闭实名", 510, 158)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1022, 730)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=826, topY=504, bottomY=561)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_qyz2(data)

    # 热门仙侠手游
    # devices.start_apk(apkPath)
    # time.sleep(50)
    # devices.AdbShellInputTap("点击更新", 808, 619)
    # time.sleep(60)
    # devices.AdbShellInputTap("点击更新", 1100, 243)
    # time.sleep(2)
    # if devices.adbDumpTap("立即登录", apkPath):
    #     time.sleep(5)
    # else:
    #     devices.adbDumpTap("账号登录", apkPath)
    #     time.sleep(2)
    #     # devices.AdbShellInputTap("账号登录", 759, 359)
    #     devices.adbDumpTap("请输入账号", apkPath)
    #     time.sleep(2)
    #     devices.AdbShellInputText("204209498 ")
    #     time.sleep(2)
    #     # devices.AdbShellInputTap("账号登录", 777, 453)
    #     devices.adbDumpTap("请输入密码", apkPath)
    #     time.sleep(2)
    #     devices.AdbShellInputText("323089 ")
    #     time.sleep(2)
    #     devices.adbDumpTap("立即登录", apkPath)
    #     time.sleep(5)
    # devices.AdbShellInputTap("关闭实名", 1086, 261)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭手机绑定", 1097, 243)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 898, 735)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # qfvalue = OCRbase(picture, isFix=True, topX=604, bottomX=880, topY=504, bottomY=590)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_qyz3(data)

    # 古剑奇谭
    # devices.start_apk(apkPath)
    # time.sleep(60)
    # devices.adbDumpTap("确认注册", apkPath)
    # time.sleep(5)
    # # devices.adbDumpTap("进入游戏", apkPath)
    # # time.sleep(5)
    # # devices.adbDumpTap("稍后填写", apkPath)
    # # time.sleep(5)
    # devices.AdbShellInputTap("关闭手机绑定", 450, 230)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1631, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 古剑奇谭
    # devices.start_apk(apkPath)
    # time.sleep(60)
    # devices.adbDumpTap("进入游戏", apkPath)
    # time.sleep(5)
    # # devices.adbDumpTap("进入游戏", apkPath)
    # # time.sleep(5)
    # # devices.adbDumpTap("稍后填写", apkPath)
    # # time.sleep(5)
    # devices.adbDumpTap("返回", apkPath)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1631, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 蛇皮操作
    # devices.start_apk(apkPath)
    # time.sleep(15)
    # devices.AdbShellInputTap("关闭启动公告", 622, 1167)
    # time.sleep(10)
    # devices.adbDumpTap("", apkPath, 'com.dalan.lgh:id/dalan_agreement_check')
    # time.sleep(2)
    # devices.adbDumpTap("帐号登录", apkPath)
    # time.sleep(2)
    # # devices.adbDumpTap("使用其他方式登录", apkPath)
    # # time.sleep(2)
    # devices.AdbShellInputText("15207676214")
    # time.sleep(2)
    # devices.adbDumpTap("密码", apkPath)
    # time.sleep(2)
    # devices.AdbShellInputText("123456")
    # time.sleep(2)
    # devices.adbDumpTap("进入游戏", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭启动公告", 622, 1167)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1, 1)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=330, bottomX=580, topY=1150, bottomY=1190)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_shj(data)

    # 建桥鬼才
    # devices.start_apk(apkPath)
    # time.sleep(100)
    # devices.adbDumpTap("快速游戏", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=800, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 你来弹我啊
    # devices.start_apk(apkPath)
    # time.sleep(100)
    # devices.adbDumpTap("快速游戏", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 全民老司机
    # devices.start_apk(apkPath)
    # time.sleep(60)
    # devices.AdbShellInputTap("账号登录", 548, 267)
    # time.sleep(2)
    # devices.clear_txt()
    # time.sleep(12)
    # devices.AdbShellInputText("t285674667 ")
    # time.sleep(2)
    # devices.AdbShellInputTap("账号登录", 660, 426)
    # time.sleep(2)
    # devices.clear_txt()
    # time.sleep(10)
    # devices.AdbShellInputText("123456 ")
    # time.sleep(2)
    # devices.adbDumpTap("进入游戏", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 山海经神兽录-安卓
    # devices.start_apk(apkPath)
    # time.sleep(60)
    # devices.adbDumpTap("游客进入", apkPath)
    # time.sleep(2)
    # devices.adbDumpTap("进入游戏", apkPath)
    # time.sleep(4)
    # devices.adbDumpTap("取消", apkPath)
    # time.sleep(3)
    # devices.AdbShellInputTap("关闭公告", 1, 1)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=330, bottomX=580, topY=1150, bottomY=1190)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_shj(data)

    # 大奉打更人
    # devices.start_apk(apkPath)
    # time.sleep(60)
    # devices.adbDumpTap("确认注册", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1454, 97)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=569, bottomX=818, topY=555, bottomY=615)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_cq(data)

    # 地藏伏魔
    # devices.start_apk(apkPath)
    # time.sleep(60)
    # devices.adbDumpTap("确认注册", apkPath)
    # time.sleep(5)
    # devices.adbDumpTap("", apkPath, "%s:id/iv_back" % name)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

    # 烧脑大师
    # devices.start_apk(apkPath)
    # time.sleep(10)
    # devices.AdbShellInputTap("关闭启动公告", 636, 701)
    # time.sleep(30)
    # devices.adbDumpTap("", apkPath, 'com.dalan.lgh:id/dalan_agreement_check')
    # time.sleep(2)
    # devices.adbDumpTap("帐号登录", apkPath)
    # time.sleep(2)
    # devices.clear_txt()
    # time.sleep(8)
    # devices.AdbShellInputText("15207676214")
    # time.sleep(2)
    # devices.AdbShellInputTap("点击密码", 575, 411)
    # time.sleep(2)
    # devices.clear_txt()
    # time.sleep(5)
    # devices.AdbShellInputText("123456")
    # time.sleep(2)
    # devices.adbDumpTap("登录", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)

   # 琉璃仙境
    devices.start_apk(apkPath)
    time.sleep(60)
    devices.adbDumpTap("", apkPath,"com.llxy.qs.cn:id/btn_login")
    time.sleep(2)
    devices.adbDumpTap("请输入账号",apkPath)
    time.sleep(2)
    devices.AdbShellInputText("uiouio")
    time.sleep(2)
    devices.adbDumpTap("请输入密码6–22位",apkPath)
    time.sleep(2)
    devices.AdbShellInputText("123456")
    time.sleep(2)
    devices.adbDumpTap("登录",apkPath)
    time.sleep(5)
    devices.AdbShellInputTap("关闭抽奖",1073,219)
    time.sleep(2)
    devices.AdbShellInputTap("关闭公告", 1022, 730)
    time.sleep(2)
    devices.AdbShellInputTap("关闭抽奖", 1073, 219)
    time.sleep(2)
    devices.AdbShellScreencapPullRm(picture)
    time.sleep(2)
    qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=826, topY=504, bottomY=561)
    time.sleep(2)
    data = qfvalue.ocr_QFdata()
    return is_notice_qyz2(data)


    # 疯狂祖安人
    # devices.start_apk(apkPath)
    # time.sleep(15)
    # devices.AdbShellInputTap("关闭启动公告", 622, 1167)
    # time.sleep(10)
    # devices.adbDumpTap("", apkPath, 'com.dalan.lgh:id/dalan_agreement_check')
    # time.sleep(2)
    # devices.adbDumpTap("帐号登录", apkPath)
    # time.sleep(2)
    # # devices.adbDumpTap("使用其他方式登录", apkPath)
    # # time.sleep(2)
    # devices.clear_txt()
    # time.sleep(5)
    # devices.AdbShellInputText("15207676214")
    # time.sleep(2)
    # devices.adbDumpTap("密码", apkPath)
    # time.sleep(2)
    # devices.AdbShellInputText("123456")
    # time.sleep(2)
    # devices.adbDumpTap("登录", apkPath)
    # time.sleep(5)
    # devices.AdbShellInputTap("关闭启动公告", 622, 1167)
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1, 1)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=330, bottomX=580, topY=1150, bottomY=1190)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice_shj(data)


    # 地藏诛魔录
    # devices.start_apk(apkPath)
    # time.sleep(100)
    # devices.adbDumpTap("账号登录", apkPath)
    # time.sleep(5)
    # devices.adbDumpTap("请输入游戏账号或手机号", apkPath)
    # time.sleep(2)
    # devices.AdbShellInputText("11095360")
    # time.sleep(2)
    # devices.adbDumpTap("请输入登录密码", apkPath)
    # time.sleep(2)
    # devices.AdbShellInputText("543811")
    # time.sleep(2)
    # devices.AdbShellInputTap("关闭公告", 1361, 89)
    # time.sleep(2)
    # devices.AdbShellScreencapPullRm(picture)
    # time.sleep(2)
    # qfvalue = OCRbase(picture, isFix=True, topX=558, bottomX=983, topY=515, bottomY=567)
    # time.sleep(3)
    # data = qfvalue.ocr_QFdata()
    # return is_notice(data)


try:
    data = rule()
    if "国" in data or "区" in data or "服" in data:
        pass
    else:
        data = rule()
    devices.log("开服数据：%s" % data)
    devices.printLog("识别区服", "开服数据：%s" % data)
    value = adb.dataRe(state=0, err="", datas=data)
    if not devices.detaillog:
        print(json.dumps(value), end=" ")
    else:
        pass
    devices.killCurrentGame(apkPath)
except FileNotFoundError as e:
    value = adb.dataRe(state=1, err=str(e), datas="")
    print(json.dumps(value), end=" ")
    devices.killCurrentGame(apkPath)
except TypeError as t:
    value = adb.dataRe(state=1, err=str(t), datas="")
    print(json.dumps(value), end=" ")
    devices.killCurrentGame(apkPath)
except AttributeError as a:
    value = adb.dataRe(state=1, err=str(a), datas="")
    print(json.dumps(value), end=" ")
    devices.killCurrentGame(apkPath)
except IndexError as i:
    value = adb.dataRe(state=1, err=str(i), datas="")
    print(json.dumps(value), end=" ")
    devices.killCurrentGame(apkPath)
except Exception as j:
    value = adb.dataRe(state=1, err=str(j), datas="")
    print(json.dumps(value), end=" ")
    devices.killCurrentGame(apkPath)
