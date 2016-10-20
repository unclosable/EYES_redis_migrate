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
        for DATA_RECORD in root.findall('DATA_RECORD'):
            mapkey = DATA_RECORD.get('DATA_KEY')
            data = {}
            for DATA_PARAM in DATA_RECORD.findall('DATA_PARAM'):
                data[DATA_PARAM.get('KEY')] = DATA_PARAM.text
            reDatas[mapkey] = data
        return reDatas


if __name__ == "__main__":
    reader = FileReaderClass(
        '/Users/zhengwei/Desktop/EYES_unfinished_ProcessStandardsActionSetKey_zvZskZkNgUv9gam0.xml')
    datas = reader.readDatas()
    # print(datas)
