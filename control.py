import argparse
from adb import AdbBase
import os
class Control(object):
	"""docstring for Control"""
	_emulatorList = {}
	def __init__(self, arg):
		super(Control, self).__init__()
		self.arg = arg

	def __run(self,cmd):
		execResult = os.popen(cmd)
		execResultStr = execResult.read()
		execResult.close()
		return execResultStr

    #返回当前模拟器列表以及对应的状态
	def getEmulatorList(self):
		result = self.__run("adb devices").strip()
		for item in result.splitlines()[1:]:
			deviceName = item.split('device')[0].strip()  
			adb = AdbBase(deviceName)
			self._emulatorList[deviceName] = adb.detectIsWorking()
		return self._emulatorList

    #返回是否安装成功
	def getDeviceInstall(self,device,path):
		adb = AdbBase(device)
		result = adb.install_apk(path)
		return {"isInstallSuceess":result}

parser = argparse.ArgumentParser(description="powered from apson")
parser.add_argument('-d','--devicelist',help='返回')
parser.add_argument('-i','--install',help='目标文件位置')



control = Control("")
args = parser.parse_args()
if args.devicelist:
	print(control.getEmulatorList())
if args.install:
	print(control.getDeviceInstall("3EP0219114001784",args.install))







