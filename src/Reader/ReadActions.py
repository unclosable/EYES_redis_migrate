from Reader.migrate import MigrateClass as MC

__filePath = '/home/deploy'
__redisHost = '10.230.4.31'
__redisPort = '6379'

# 测试库
# __filePath = '/Users/zhengwei/Desktop'
# __redisHost = '10.3.47.20'
# __redisPort = '10000'

collect = MC(filePath=__filePath,
             setKey='eyes_collect',
             mapKeys=['id', 'step', 'opt_at', 'deadline', 'isCollectOrWayBill'],
             redisHost=__redisHost,
             redisPort=__redisPort,
             mapkey_Prefix='collect_')

sorting = MC(filePath=__filePath,
             setKey='EYES_UnStepedSortingOrderSet_',
             mapKeys=['value', 'limtTime'],
             redisHost=__redisHost,
             redisPort=__redisPort)

order1 = MC(filePath=__filePath,
            setKey='EYES_unfinished_ProcessStandardsActionSetKey_zvZskZkNgUv9gam0',
            mapKeys=['ProcessStandardsAction_limitType',
                     'ProcessStandardsAction_limitId',
                     'ProcessStandardsAction_startTime',
                     'ProcessStandardsAction_warnTime',
                     'ProcessStandardsAction_limitEndTime',
                     'ProcessStandardsAction_data'],
            redisHost=__redisHost,
            redisPort=__redisPort)

order2 = MC(filePath=__filePath,
            setKey='EYES_unfinished_ProcessStandardsActionSetKey_kUQ1wcxnvoMoaFJN',
            mapKeys=['ProcessStandardsAction_limitType',
                     'ProcessStandardsAction_limitId',
                     'ProcessStandardsAction_startTime',
                     'ProcessStandardsAction_warnTime',
                     'ProcessStandardsAction_limitEndTime',
                     'ProcessStandardsAction_data'],
            redisHost=__redisHost,
            redisPort=__redisPort)

actions = [collect, sorting, order1, order2]

if __name__ == '__main__':
    for i in range(len(actions)):
        actions[i].redData()
