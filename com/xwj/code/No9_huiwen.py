# -*-coding:utf-8 -*-
'''回文数判断'''
from sqlalchemy.sql.expression import false


def isPalindrome(x):
    # 转成list
    result = []
    res = []
    if x < 0:  # 负数
        return False
    else:
        while x // 10:
            result.append(x % 10)
            res.append(x % 10)
            x = x // 10
        result.append(x % 10)
        res.append(x % 10)
        print(result)
        res.reverse()
        print(res)
        for i in range(len(result)):
            if res[i] != result[i]:
                return False
        return True


def isPalindrome1(x):
    z = x
    y = 0
    while x > 0:
        y = y * 10 + x % 10
        x = x // 10
    return z == y


def isPalindrome2(x):
    if x < 0:
        return False
    elif x % 10 == 0 and x != 0:
        return False
    revertedNumber = 0
    while(x > revertedNumber):
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10
#    当为奇数时revertedNumber//10可以出去中位数字
    return x == revertedNumber or x == revertedNumber // 10


if __name__ == '__main__':
    s = 1000021
    print(s // 10, s % 10)
    print(s // 10, s % 10)
    result = isPalindrome2(s)
    print("原来的数%s" % s)
    print("反转之后为：%s" % result)
