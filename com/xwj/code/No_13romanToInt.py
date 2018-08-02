# -*-coding:utf-8 -*-
'''将罗马数字转整数'''


def romanToInt(s):
    return 0
# 将整数转成罗马


def intToRoman(num):
    roman = ''
    if num == 4:
        roman = 'IV'


if __name__ == '__main__':
    s = 1000021
    print(s // 10, s % 10)
    print(s // 10, s % 10)
    result = romanToInt(s)
    print("原来的数%s" % s)
    print("反转之后为：%s" % result)
