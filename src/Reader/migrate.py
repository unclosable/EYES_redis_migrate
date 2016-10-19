import redis
from fileHandler.XMLFileWriter import FileWriterClass as FW
from fileHandler.XMLFileReader import FileReaderClass as FR


class MigrateClass(object):
    __filePath__ = None
    __setKey__ = None
    __mapKeys__ = None
    __redisHost__ = None
    __redisPort__ = None
    __redisPassword__ = None
    __mapkey_Prefix__ = None

    __redisClient__ = None

    def __init__(self, filePath, setKey, mapKeys, redisHost, redisPort, mapkey_Prefix=None, redisPassword=None):
        self.__filePath__ = filePath
        self.__setKey__ = setKey
        self.__mapKeys__ = mapKeys
        self.__redisHost__ = redisHost
        self.__redisPort__ = redisPort
        self.__redisPassword__ = redisPassword

        if mapkey_Prefix is not None:
            self.__mapkey_Prefix__ = mapkey_Prefix
        else:
            self.__mapkey_Prefix__ = ''

    def __redis_check__(self):
        if self.__redisClient__ is None:
            try:
                self.__redisClient__ = redis.Redis(host=self.__redisHost__, port=self.__redisPort__,
                                                   password=self.__redisPassword__)
            except:
                print('[' + self.__redisHost__ + ':' + self.__redisPort__ + ']REDIS连接失败')
                return False
        return True

    def redData(self):
        if not self.__redis_check__():
            return
        set = self.__redisClient__.smembers(self.__setKey__)
        file = FW(self.__filePath__ + '/' + self.__setKey__ + '.xml')
        for key in set:
            mapkey = self.__mapkey_Prefix__ + key.decode('utf-8')
            data = {}
            dataList = self.__redisClient__.hmget(mapkey, self.__mapKeys__)
            for i in range(len(self.__mapKeys__)):
                if dataList[i] is not None:
                    data[self.__mapKeys__[i]] = dataList[i].decode('utf-8')
            file.write(key.decode('utf-8'), data=data)
        file.flush()
        print(str(len(set)) + '条读取数据＝》' + self.__filePath__ + '/' + self.__setKey__ + '.xml')

    def writeData(self):
        if not self.__redis_check__():
            return
        file = FR(self.__filePath__ + '/' + self.__setKey__ + '.xml')
        datas = file.readDatas()
        index = 0
        for key in datas:
            try:
                self.__redisClient__.sadd(self.__setKey__, key)
                self.__redisClient__.hmset(self.__mapkey_Prefix__ + key, datas[key])
            except:
                print('失败')
                print(key)
                print(datas[key])
                continue
            index += 1
        print(str(index) + '条写入数据《＝' + self.__filePath__ + '/' + self.__setKey__ + '.xml')


if __name__ == '__main__':
    MC = MigrateClass(filePath='/Users/zhengwei/Desktop', setKey='eyes_collect',
                      mapKeys=['id', 'step', 'opt_at', 'deadline', 'isCollectOrWayBill'],
                      redisHost='10.3.47.20', redisPort='10000', mapkey_Prefix='collect_')
    MC.redData()
    # MC.writeData()
