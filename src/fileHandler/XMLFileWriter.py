import xml.etree.cElementTree as ET


class FileWriterClass(object):
    __path__ = None
    __root__ = None

    def __init__(self, path):
        self.__path__ = path
        self.__initRoot__()

    def __initRoot__(self):
        self.__root__ = ET.Element('ROOT')

    def __writeData__(self, nodeName, data):
        document = ET.Element('DATA_RECORD')
        document.set('DATA_KEY', nodeName)
        for key in data:
            node = ET.Element('DATA_PARAM')
            node.set('KEY', str(key))
            node.text = str(data[key])
            # ET.SubElement(document, node)
            document.append(node)
        self.__root__.append(document)
        # ET.SubElement(self.__root__, document)

    def __writeDataList__(self, datas):
        for i in range(len(datas)):
            self.__writeData__(datas[i])

    def write(self, nodeName, data=None):
        if data is not None:
            self.__writeData__(nodeName, data)

    def flush(self):
        tree = ET.ElementTree(self.__root__)
        tree.write(self.__path__)
        # print(ET.dump(self.__root__))


if __name__ == "__main__":
    # list = [{'a': 'a'}, {'b': 'b'}]
    writer = FileWriterClass('/Users/zhengwei/Desktop/test.xml');
    for i in range(1):
        data = {'id': i, 'step': i, 'opt_at': i, 'deadline': i, 'isCollectOrWayBill': i}
        writer.write('DATAMAP_' + str(i), data=data)
    writer.flush()
