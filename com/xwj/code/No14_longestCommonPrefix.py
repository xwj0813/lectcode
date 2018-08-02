# -*- coding:utf-8 -*-
'''寻找字符组中最长的公共前缀'''
from functools import reduce
import sys


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    print(strs)
    # print(min(strs, key=len))
    minlength = sys.maxsize
    for c in strs:
        if len(c) < minlength:
            minlength = len(c)

    result = []
    print(len(result))
    flag = True
    string = strs[0]
    for j in range(minlength):
        char = string[j]
        print("char", char, type(char))
        for i in range(1, len(strs)):
            if char not in strs[i][j]:
                flag = False
        print("flag", flag)
        if flag:
            result.append(char)
    if len(result) == 0:
        return ""
    else:
        return ''.join(result)
#     if strs.isalnum() and strs.islower():  # 都是小写并且都是字母


def longestCommonPrefix1(strs):
    if len(strs) == 0:
        return ""

    result = []

    flag = True
    string = min(strs, key=len)
    for j in range(len(string)):
        char = string[j]
        print("char", char, type(char))
        for i in range(1, len(strs)):
            if char not in strs[i][j]:
                flag = False
        print("flag", flag)
        if flag:
            result.append(char)
    if len(result) == 0:
        return ""
    else:
        return ''.join(result)


if __name__ == '__main__':
    strs = ["aas", "a", "acd"]
    s = longestCommonPrefix1(strs)
    print('s', s)
