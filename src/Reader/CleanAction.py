import redis
from multiprocessing.pool import ThreadPool

__redisHost = '10.230.4.31'
__redisPort = '6379'
__setKeys = ['eyes_collect', 'EYES_UnStepedSortingOrderSet_',
             'EYES_unfinished_ProcessStandardsActionSetKey_zvZskZkNgUv9gam0',
             'EYES_unfinished_ProcessStandardsActionSetKey_kUQ1wcxnvoMoaFJN']


def __deletekey__(redisClient, key):
    redisClient.delete(key)


def __clean__(key):
    redisPool = redis.ConnectionPool(host=__redisHost, port=__redisPort)
    redisClient = redis.Redis(connection_pool=redisPool)

    set = redisClient.smembers(key)

    pool = ThreadPool(processes=10)
    print(key + ':::' + str(len(set)) + '条数据将清除')
    for mapkey in set:
        pool.apply_async(__deletekey__, (redisClient, mapkey))
    pool.apply_async(__deletekey__, (redisClient, key))
    pool.close()
    pool.join()
    print(key + ':::' + str(len(set)) + '条数据已清除')


def clean():
    for key in __setKeys:
        __clean__(key)
