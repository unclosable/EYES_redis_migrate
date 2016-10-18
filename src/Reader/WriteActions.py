from Reader.migrate import MigrateClass as MC

__filePath = '/home/deploy'
__redisHost = 'redis.rfddc.com'
__redisPort = '8003'
__password = 'redis_001_004'

# 测试库
# __filePath = '/Users/zhengwei/Desktop'
# __redisHost = '10.3.47.20'
# __redisPort = '10000'
# __password = None

collect = MC(filePath=__filePath,
             setKey='eyes_collect',
             mapKeys=['id', 'step', 'opt_at', 'deadline', 'isCollectOrWayBill'],
             redisHost=__redisHost,
             redisPort=__redisPort,
             mapkey_Prefix='collect_',
             redisPassword=__password)

sorting = MC(filePath=__filePath,
             setKey='EYES_UnStepedSortingOrderSet_',
             mapKeys=['value', 'limtTime'],
             redisHost=__redisHost,
             redisPort=__redisPort,
             redisPassword=__password)

order1 = MC(filePath=__filePath,
            setKey='EYES_unfinished_ProcessStandardsActionSetKey_zvZskZkNgUv9gam0',
            mapKeys=['ProcessStandardsAction_limitType',
                     'ProcessStandardsAction_limitId',
                     'ProcessStandardsAction_startTime',
                     'ProcessStandardsAction_warnTime',
                     'ProcessStandardsAction_limitEndTime',
                     'ProcessStandardsAction_data'],
            redisHost=__redisHost,
            redisPort=__redisPort,
            redisPassword=__password)

order2 = MC(filePath=__filePath,
            setKey='EYES_unfinished_ProcessStandardsActionSetKey_kUQ1wcxnvoMoaFJN',
            mapKeys=['ProcessStandardsAction_limitType',
                     'ProcessStandardsAction_limitId',
                     'ProcessStandardsAction_startTime',
                     'ProcessStandardsAction_warnTime',
                     'ProcessStandardsAction_limitEndTime',
                     'ProcessStandardsAction_data'],
            redisHost=__redisHost,
            redisPort=__redisPort,
            redisPassword=__password)

actions = [collect, sorting, order1, order2]

if __name__ == '__main__':
    for i in range(len(actions)):
        actions[i].writeData()
