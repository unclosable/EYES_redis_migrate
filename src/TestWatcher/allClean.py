import redis

__redisPool__ = redis.ConnectionPool(host='10.3.47.20', port='10000')
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
    __rc__.delete('EYES_TOTLE_ORDERACTION_COUNTER_MAPKEY_1063YE4LJJA5S3UM')
    limitKeyList = __rc__.smembers('EYES_LIMIT_COUNTER_SETKEY_EqOH6SQD3OX12efd')
    for limitKey in limitKeyList:
        __rc__.delete(limitKey)
    # __rc__.delete('EYES_LIMIT_COUNTER_SETKEY_EqOH6SQD3OX12efd')
    for key in types:
        __rc__.delete('EYES_LIMIT_DEFAULT_COUNTER_MAPKEY_' + key)
    __rc__.delete('EYES_LIMIT_DEFAULT_COUNTER_SETKEY_OQK86USRS7N88AY6')
