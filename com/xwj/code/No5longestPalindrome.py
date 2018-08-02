# -*- coding:utf-8 -*-

'''给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。'''


def longestPalindrome(s):
    start = 0
    end = 0
    if len(s) < 2:
        return s
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        lens = max(len1, len2)
        print(lens)
        if lens > (end - start):
            start = i - (lens - 1) // 2
            end = i + lens // 2
        print(start, end)
    return s[start:end + 1]


def expandAroundCenter(s, left, right):
    while left > 0 and right < len(s) and s[left] == s[right]:
        left = left - 1
        right = right + 1
    return right - left - 1


def longestPalindrome1(s):
    """
    :type s: str
    :rtype: str
    """
    # 小詹提示：这种题要注意特例，单字符本身就是自己的最大回文子串噢
    print(s)
    if len(s) < 2:
        return s
    # 定义待返回的字符串
    res = ""
    for i in range(len(s)):
        # 这里就是考虑到两种情况，从相同字符拓宽和从相邻字符拓宽
        helper(res, s, i, i)
        helper(res, s, i, i + 1)
    return res

# 分割出来的相同操作函数！


def helper(res, s, left, right):
    # 这里是判断当前回文子串两端相同的时候，向两端拓展
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
        # 这里的right-left-1是当前的回文子串长度，大于历史最大值，就更新最大值
    if right - left - 1 > len(res):
        res = s[left + 1:right]


if __name__ == '__main__':
    s = "ab"
    result = longestPalindrome1(s)
    print(result)
