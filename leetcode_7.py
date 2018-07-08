# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_7
@time: 2018/7/1 下午1:05

给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:
输入: 123
输出: 321

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            return num_handle(int(str(x)[::-1]))
        else:
            return num_handle(-int(str(-x)[::-1]))


def num_handle(x):
    if x > 2 ** 31 - 1 or x < - 2 ** 31:
        return 0
    return x


solution = Solution()
print solution.reverse(532)
