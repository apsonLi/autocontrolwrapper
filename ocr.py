from aip import AipOcr

APP_ID = '17975398'
API_KEY = 'n8bGMLwndukfywu18yKLuNYI'
SECRET_KEY = 'fNqBSM0A9gRloci2kv139ZlxL7aGSfor'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# basicAccurate 高精准 basicGeneral 通用
def ocr_data(path):
    image = get_file_content(path)
    resluts = client.basicAccurate(image)
    # print(resluts)
    return resluts["words_result"][0]["words"]

# print(ocr_data(r"D:\PyCharm\space\testApi\picture\hmy2.png"))
