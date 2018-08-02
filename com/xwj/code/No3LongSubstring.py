#-*- coding:utf-8 -*-
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxlen = 0
    if len(s) <= 1:
        maxlen = len(s)

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[j] in s[i:j]:
                if j - i > maxlen:
                    right = j
                    left = i
                    maxlen = right - left
                break

            elif j == len(s) - 1:
                if maxlen < j - i + 1:
                    maxlen = j - i + 1

    return maxlen


if __name__ == '__main__':
    test = "abcabcbb"
    result = lengthOfLongestSubstring(test)
    print(result)
