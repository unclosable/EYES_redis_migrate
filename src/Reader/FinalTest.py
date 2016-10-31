import redis


def testAction():
    rc = redis.Redis(host='redis.rfddc.com', port='8003', password='redis_001_004')
    print('eyes_collect')
    print(rc.scard('eyes_collect'))
    print('EYES_UnStepedSortingOrderSet_')
    print(rc.scard('EYES_UnStepedSortingOrderSet_'))
    print('EYES_unfinished_ProcessStandardsActionSetKey_zvZskZkNgUv9gam0')
    print(rc.scard('EYES_unfinished_ProcessStandardsActionSetKey_zvZskZkNgUv9gam0'))
    print('EYES_unfinished_ProcessStandardsActionSetKey_kUQ1wcxnvoMoaFJN')
    print(rc.scard('EYES_unfinished_ProcessStandardsActionSetKey_kUQ1wcxnvoMoaFJN'))


if __name__ == '__main__':
    print('TEST RUN')
    testAction()
