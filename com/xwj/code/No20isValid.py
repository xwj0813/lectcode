#-*- coding：utf-8 -*-
'''给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。'''


def isValid(s):
    if s == '':
        return True
    else:
        q = []  # 表示一个空栈
        # 如果是（，[,{则入栈
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '['or s[i] == '{' or len(q) == 0:
                q.append(s[i])
            else:
                # 从顶元素判断
                temp = q[-1]
                if s[i] == ')' and temp == '(':  # （）配对成功
                    q.pop()
                elif s[i] == ']' and temp == '[':
                    q.pop()
                elif s[i] == '}' and temp == '{':
                    q.pop()
                else:
                    q.append(s[i])
        # 如果q为空则正确
        print(q)
        if q:
            return False
        else:

            return True

        return


if __name__ == '__main__':
    digits = '{}'
    result = isValid(digits)
    print(result)
