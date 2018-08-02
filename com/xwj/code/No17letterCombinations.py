# -*- coding:utf-8 -*-
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合
'''


def letterCombinations(digits):
    dict = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
    result = ['']
    for digit in digits:
        str_digit = []
        for char in dict[digit]:
            str_digit += [x + char for x in result]
        result = str_digit
    return result


if __name__ == '__main__':
    digits = '235'
    result = letterCombinations(digits)
    print(result)
