import redis
from multiprocessing.pool import ThreadPool
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
                __redisPool = redis.ConnectionPool(host=self.__redisHost__, port=self.__redisPort__,
                                                   password=self.__redisPassword__)
                self.__redisClient__ = redis.Redis(connection_pool=__redisPool)
            except:
                print('[' + self.__redisHost__ + ':' + self.__redisPort__ + ']REDIS连接失败')
                return False
        return True

    def redData(self):
        if not self.__redis_check__():
            return
        print('开始读取')
        print(self.__filePath__ + '/' + self.__setKey__ + '.xml《＝'
              + self.__redisHost__ + ':' + self.__redisPort__ + '/' + self.__setKey__)
        set = self.__redisClient__.smembers(self.__setKey__)
        setLen = len(set)
        print('[' + self.__setKey__ + ']读取[' + str(setLen) + ']条数据')
        file = FW(self.__filePath__ + '/' + self.__setKey__ + '.xml')
        pool = ThreadPool(processes=10)
        poolResult = {}
        for key in set:
            poolResult[key] = pool.apply_async(self.__readData__, (key,))
        pool.close()
        pool.join()
        index = 0
        for key in poolResult:
            data = poolResult[key].get()
            file.write(key.decode('utf-8'), data=data)
            index += 1
        file.flush()
        print(str(index) + '条读取数据＝》' + self.__filePath__ + '/' + self.__setKey__ + '.xml')

    def __readData__(self, key):
        mapkey = self.__mapkey_Prefix__ + key.decode('utf-8')
        data = {}
        dataList = self.__redisClient__.hmget(mapkey, self.__mapKeys__)
        for i in range(len(self.__mapKeys__)):
            if dataList[i] is not None:
                data[self.__mapKeys__[i]] = dataList[i].decode('utf-8')
        return data

    def writeData(self):
        if not self.__redis_check__():
            return
        print('开始写入')
        print(self.__filePath__ + '/' + self.__setKey__ + '.xml＝》'
              + self.__redisHost__ + ':' + self.__redisPort__ + '/' + self.__setKey__)
        file = FR(self.__filePath__ + '/' + self.__setKey__ + '.xml')
        datas = file.readDatas()
        pool = ThreadPool(processes=10)
        index = 0
        for key in datas:
            if index % 50000 == 0:
                print(index)
            pool.apply_async(self.__writeData__, (key, datas[key]))
            index += 1
        pool.close()
        pool.join()
        print(str(index) + '条写入数据《＝' + self.__filePath__ + '/' + self.__setKey__ + '.xml')

    def __writeData__(self, key, data):
        try:
            self.__redisClient__.sadd(self.__setKey__, key)
            self.__redisClient__.hmset(self.__mapkey_Prefix__ + key, data)
        except:
            if data != {}:
                print('失败')
                print(key)
                print(data)


if __name__ == '__main__':
    MC = MigrateClass(filePath='/Users/zhengwei/Desktop', setKey='eyes_collect',
                      mapKeys=['id', 'step', 'opt_at', 'deadline', 'isCollectOrWayBill'],
                      redisHost='10.3.47.20', redisPort='10000', mapkey_Prefix='collect_')
    MC.redData()
    # MC.writeData()
