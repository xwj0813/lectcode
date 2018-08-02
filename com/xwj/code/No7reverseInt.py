#-*-coding :utf-8 -*-
"""给定一个32位有符号整数，将整数中的数字进行反转"""


def reverseInt(x):
    # 转换成列表
    #     ss = list(map(int, str(x)))
    result = []
    ss = list(str(x))
    if x < 0:  # 为负数
        result.append(ss[0])
        temp = ss[1:]
    else:
        temp = ss

    temp.reverse()  # 反转
    print(x, temp)
    j = 0
    for i in range(len(temp)):
        if temp[i] == 0:
            j = i
            break
    result.extend(temp[j:])

    # 转换成int型
    strr = ''.join(result)
    print("字符型：", strr)
    result_int = int(strr)
    if result_int > -(2**31) - 1 and result_int < 2**31:
        return result_int
    else:
        return 0


if __name__ == '__main__':
    s = 123
    result = reverseInt(s)
    print("原来的数%s" % s)
    print("反转之后为：%s" % result)
