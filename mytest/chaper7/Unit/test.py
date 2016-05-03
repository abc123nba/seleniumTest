#coding=utf-8
import sys
sys.path.append("./chaper7/Unit")
from count import Count

#测试两个整数相加
class TestCount:
    def test_add(self):
        try:
            j = Count(2, 4)
            add = j.add()
            assert(add == 6), 'Integer addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print('test pass!')

#执行测试类的测试方法
mytest = TestCount()
mytest.test_add()