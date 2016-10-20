import redis
from multiprocessing.pool import ThreadPool
from fileHandler.XMLFileWriter import FileWriterClass
from fileHandler.XMLFileReader import FileReaderClass


def redData():
    redisClient = redis.Redis(host='10.3.47.20', port='10000', password='')

    setKey = 'eyes_collect'

    mapKeys = ['id', 'step', 'opt_at', 'deadline', 'isCollectOrWayBill']
    set = redisClient.smembers(setKey)
    file = FileWriterClass(setKey + '.xml')
    for key in set:
        mapkey = 'collect_' + key.decode('utf-8')
        data = {}
        dataList = redisClient.hmget(mapkey, mapKeys)
        # print(mapkey)
        # print(dataList)
        for i in range(len(mapKeys)):
            if dataList[i] is not None:
                data[mapKeys[i]] = dataList[i].decode('utf-8')
        file.write(key.decode('utf-8'), data=data)
    file.flush()


__setKey = 'TESTDATA_EYES'
__redisPool = redis.ConnectionPool(host='10.3.47.20', port='10000')
__redisClient = redis.Redis(connection_pool=__redisPool)


def __writeData__(redisClient, key, data):
    redisClient.sadd(__setKey, key)
    redisClient.hmset(key, data)


def writeData():
    # redisClient = redis.Redis(host='10.3.47.20', port='10000')

    # file = FileReaderClass(setKey + '.xml')
    file = FileReaderClass('/Users/zhengwei/Desktop/test3.xml')  # 测试源数据
    datas = file.readDatas()
    pool = ThreadPool(processes=10)
    print(datas)
    for key in datas:
        pool.apply(__writeData__, (__redisClient, key, datas[key]))
        # redisClient.sadd(setKey, key)
        # print(key)
        # print(datas[key])
        # redisClient.hmset('collect_' + key, datas[key])


def __clean__():
    # redisClient = redis.Redis(host='10.3.47.20', port='10000')

    set = __redisClient.smembers(__setKey)

    pool = ThreadPool(processes=10)
    for key in set:
        print(key)
        pool.apply(__deletekey__, (__redisClient, key))
        # redisClient.delete(key)
    # redisClient.delete(__setKey)
    pool.apply(__deletekey__, (__redisClient, __setKey))


def __deletekey__(redisClient, key):
    redisClient.delete(key)


def __test__():
    # bkey = b'com.xiaojiuwo.models.ProcessStandardsAction[waybillId=11610186309832]'
    # key = 'com.xiaojiuwo.models.ProcessStandardsAction[waybillId=11610186309832]'
    # redisClient = redis.Redis(host='10.3.47.20', port='10000')
    # redisClient.hmset(bkey, {'test': 'test'})
    print(__redisClient.hgetall(b'com.xiaojiuwo.entities.SortingLimtResult[46327920]'))
    print(__redisClient.hgetall('com.xiaojiuwo.entities.SortingLimtResult[46327920]'))
    # redisClient.delete(bkey)


if __name__ == "__main__":
    # writeData()
    # redData()
    __clean__()
    # __test__()
