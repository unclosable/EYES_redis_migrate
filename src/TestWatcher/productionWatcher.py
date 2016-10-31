import redis

__redisPool__ = redis.ConnectionPool(host='redis.rfddc.com', port='8003',
                                     password='redis_001_004')
__rc__ = redis.Redis(connection_pool=__redisPool__)

types = {"Site_TakeOverOrder": "揽件时效",
         "Transport_CenterToSite": "分拣中心到站点时效",
         "Transport_BetweenCity": "城际运输时效",
         "Site_SortingOrder": "分拣时效",
         "Site_SendOrder": "配送时效",
         "Site_AllOrder": "总时效",
         "Transport_SiteToCenter": "站点到分拣中心时效",
         "Transport_PartyBetweenCity": "三方城际运输"}

if __name__ == '__main__':
    print('__________________________')
    print('         总计数器          ')
    map = __rc__.hgetall('EYES_TOTLE_ORDERACTION_COUNTER_MAPKEY_1063YE4LJJA5S3UM')
    for key in map:
        print(types[key.decode()] + ':' + map[key].decode())
    print('__________________________')
    print('           校验            ')
    limitKeyList = __rc__.smembers('EYES_LIMIT_COUNTER_SETKEY_EqOH6SQD3OX12efd')
    for limitKey in limitKeyList:
        print('LIMIT_KEY:' + limitKey.decode())
        limitMap = __rc__.hgetall(limitKey)
        for limitMapKey in limitMap:
            print('     ' + limitMapKey.decode() + ':' + limitMap[limitMapKey].decode())
    print('__________________________')
    print('         省缺校验          ')
    for key in types:
        defaltMap = __rc__.hgetall('EYES_LIMIT_DEFAULT_COUNTER_MAPKEY_' + key)
        if defaltMap != {}:
            print(types[key])
        for deKey in defaltMap:
            print('     ' + deKey.decode() + ':' + defaltMap[deKey].decode())
    print('__________________________')
