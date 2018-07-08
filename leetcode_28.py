# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_28
@time: 2018/7/8 下午8:27
使用python库实现
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle == "":
        #     return 0
        return haystack.find(needle)


solution = Solution()

print solution.strStr("123", "")
