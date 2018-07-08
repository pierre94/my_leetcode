# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_20
@time: 2018/7/8 下午3:35

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return valid_check(s)


def valid_check(s):
    if s == "":
        return True
    for i in range(0, len(s)):
        for j in range(len(s) - 1, -1, -1):
            if i == j:
                return False
            if s[j] == _dict.get(s[i], None):
                print "s[j]:", s[j], "j:", j
                print "s[i]:", s[i], "i:", i
                _new_str = ""
                for t in range(0, len(s)):
                    if t == i or t == j:
                        pass
                    else:
                        _new_str = _new_str + s[t]
                print "_new_str:", _new_str
                return valid_check(_new_str)


_dict = {"(": ")", "[": "]", "{": "}"}
# # _str = "()[]{}"
# _str = "{[]}"
_str = "([)]"
solution = Solution()
print solution.isValid(_str)
# 逻辑有问题，请直接看leetcode_20_with_stack.py
