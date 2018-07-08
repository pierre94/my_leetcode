# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_14
@time: 2018/7/8 下午2:33

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入: ["flower","flow","flight"]
输出: "fl"
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = []
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(0, len(strs[0])):
            for item in strs:
                if i > (len(item) - 1):
                    return ("").join(common_prefix)
                if item[i] != (strs[0])[i]:
                    return ("").join(common_prefix)
            common_prefix.append((strs[0])[i])
        if common_prefix == []:
            return ""
        else:
            return ("").join(common_prefix)


# strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]
strs = ["a"]
solution = Solution()
print solution.longestCommonPrefix(strs)
