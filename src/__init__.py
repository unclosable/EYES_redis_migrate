import sys
from Reader.ReadActions import readActions as READ
from Reader.WriteActions import writeActions as WRITE
from Reader.TestActions import testAction

if __name__ == '__main__':
    if len(sys.argv) > 1:
        actType = sys.argv[1]
        if actType == "READ":
            for i in range(len(READ)):
                READ[i].redData()
        elif actType == "WRITE":
            for i in range(len(WRITE)):
                WRITE[i].writeData()
        elif actType == 'TEST':
            testAction()
        else:
            print('非法参数' + actType)
    else:
        print('需要参数"READ"或者"WRITE"或者"TEST"')
