# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_20_with_stack
@time: 2018/7/8 下午4:46
"""


class Stack:
    """模拟栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        stack = []
        d = ["()", "[]", "{}"]
        for i in range(0, len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2] + stack[-1] in d:
                print stack
                stack.pop()
                print stack
                stack.pop()
        return len(stack) == 0


# _str = "([)]"
_str = "{()[]}"
# _str = "[]{}()"
solution = Solution()
print solution.isValid(_str)
