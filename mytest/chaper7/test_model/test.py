#coding=utf-8
import sys
sys.path.append("./chaper7/test_model")
from count110 import Count119

#测试两个整数相加
class TestCount:
    def test_add(self):
        try:
            j = Count119(2, 4)
            add = j.add()
            assert(add == 6), 'Integer addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print('test pass!')

#执行测试类的测试方法
mytest = TestCount()
mytest.test_add()