import redis
from fileHandler.XMLFileWriter import FileWriterClass
from fileHandler.XMLFileReader import FileReaderClass


def redData():
    redisClient = redis.Redis(host='10.3.47.20', port='10000',password='')

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


def writeData():
    redisClient = redis.Redis(host='10.3.47.20', port='10000')

    setKey = 'eyes_collect'

    # file = FileReaderClass(setKey + '.xml')
    file = FileReaderClass('/Users/zhengwei/Desktop/test.xml')  # 测试源数据
    datas = file.readDatas()

    for key in datas:
        redisClient.sadd(setKey, key)
        # print(key)
        # print(datas[key])
        redisClient.hmset('collect_' + key, datas[key])


def __clean__():
    redisClient = redis.Redis(host='10.3.47.20', port='10000')

    setKey = 'eyes_collect'

    set = redisClient.smembers(setKey)

    for key in set:
        redisClient.delete(key)
    redisClient.delete(setKey)


if __name__ == "__main__":
    # writeData()
    redData()
    # __clean__()
