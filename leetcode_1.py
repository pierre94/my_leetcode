# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_1
@time: 2018/6/30 下午12:52

粗暴实现，推荐使用hash表
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if ((nums[i] + nums[j]) == target) and (i != j):
                    return [i, j]
