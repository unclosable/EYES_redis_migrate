import redis
from socketIO_client import SocketIO
import json

__redisPool__ = redis.ConnectionPool(host='redis.rfddc.com', port='8003',
                                     password='redis_001_004')
__rc__ = redis.Redis(connection_pool=__redisPool__)

if __name__ == '__main__':
    datamap = __rc__.hgetall('EYES_TOTLE_ORDERACTION_COUNTER_MAPKEY_1063YE4LJJA5S3UM')
    socketIO = SocketIO('https://message.wuliusys.com');
    emitMap = {}
    for key in datamap:
        emitMap[key.decode()] = datamap[key].decode()
    print(json.dumps(emitMap))
    socketIO.emit("OrderActionCount", json.dumps(emitMap))
    socketIO.wait(seconds=1)
    socketIO.disconnect()
