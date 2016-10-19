import xml.etree.cElementTree as ET


class FileReaderClass(object):
    filePath = ''
    datas = []

    def __init__(self, filePath):
        self.filePath = filePath

    def readDatas(self):
        tree = ET.parse(self.filePath)
        root = tree.getroot()
        reDatas = {}
        index = 0
        erro = 0
        for DATA_RECORD in root.findall('DATA_RECORD'):
            index += 1
            mapkey = DATA_RECORD.get('DATA_KEY')
            data = {}
            for DATA_PARAM in DATA_RECORD.findall('DATA_PARAM'):
                data[DATA_PARAM.get('KEY')] = DATA_PARAM.text
            if mapkey == 'com.xiaojiuwo.models.ProcessStandardsAction[waybillId=10510190000316]':
                print(mapkey)
                print(data)
                print(index)
                erro += 1
        print(erro)
        # reDatas[mapkey] = data
        # return reDatas


if __name__ == "__main__":
    reader = FileReaderClass(
        '/Users/zhengwei/Desktop/EYES_unfinished_ProcessStandardsActionSetKey_zvZskZkNgUv9gam0.xml')
    datas = reader.readDatas()
    # print(datas)
