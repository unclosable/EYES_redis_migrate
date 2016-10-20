from fileHandler.XMLFileWriter import FileWriterClass as FW
from fileHandler.XMLFileReader import FileReaderClass as FR

if __name__ == '__main__':
    fileR = FR('/Users/zhengwei/Desktop/EYES_unfinished_ProcessStandardsActionSetKey_kUQ1wcxnvoMoaFJN.xml')
    # fileW = FW('/Users/zhengwei/Desktop/TESTDATA.xml')

    datas = fileR.readDatas()
    index = 0
    for key in datas:
        # if index > 100000:
        #     break
        # fileW.write(key, data=datas[key])
        index += 1
    # fileW.flush()
    print(index)