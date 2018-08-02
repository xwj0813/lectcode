#-*-coding :utf-8 -*-
"""给定一个32位字符串，转换成int"""
from sqlalchemy.sql.expression import false


def myAtoi(x):
    result = 0
    flag = 1
    x = x.lstrip()  # 截掉左边的空格
    if x == '':
        return 0
    elif x[0].isalpha():
        return 0
    else:
        # 判断是不是数字
        if x[0] == '-':
            flag = -1
            x = x[1:]
        elif x[0] == '+':
            flag = 1
            x = x[1:]

        for i in range(len(x)):
            if x[i].isdigit():
                result = result * 10 + int(x[i])
            else:
                break

    print(result)
    if flag < 0:
        result = result * (-1)
    else:
        result = result

    if result < -2147483648:
        return -2147483648
    elif result > 2147483647:
        return 2147483647
    else:
        return result


if __name__ == '__main__':
    s = "  +1"
    result = myAtoi(s)
    print("原来的数%s" % s)
    print("反转之后为：%s" % result)
