from aip import AipOcr

_APP_ID = '17975398'
_API_KEY = 'n8bGMLwndukfywu18yKLuNYI'
_SECRET_KEY = 'fNqBSM0A9gRloci2kv139ZlxL7aGSfor'
_client = AipOcr(_APP_ID, _API_KEY, _SECRET_KEY)


class OCRbaidu:
    def __init__(self, filepath):
        self.filepath = filepath

    def _get_file_content(self):
        with open(self.filepath, 'rb') as fp:
            return fp.read()

    # basicAccurate 高精准 basicGeneral 通用
    # 高精准识别图片用于识别区服，不带坐标
    def ocr_QFdata(self):
        image = self._get_file_content()
        resluts = _client.basicAccurate(image)
        # print(resluts)
        return resluts["words_result"][0]["words"]

    # 返回坐标 普通版
    def ocr_Tap(self, value):
        tap = []
        image = self._get_file_content()
        result = _client.general(image)
        data = result["words_result"]

        for i in data:
            if value in i['words']:
                tap.append(i["location"]["left"])
                tap.append(i["location"]["top"])
                return tap

    # 返回坐标 精准版
    def ocr_Tap2(self, value):
        tap = []
        image = self._get_file_content()
        result = _client.accurate(image)
        data = result["words_result"]

        for i in data:
            if value in i['words']:
                tap.append(i["location"]["left"])
                tap.append(i["location"]["top"])
                return tap


# 测试
# print(OCRbaidu(r"D:\PyCharm\space\testApi\picture\hmy2.png").ocr_QFdata())
# print(OCRbaidu(r"D:\PyCharm\space\testApi\picture\hmy.png").ocr_Tap("进入游戏"))
