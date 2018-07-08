# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_27
@time: 2018/7/8 下午8:17
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # low = 0
        # l = len(nums)
        # for i in range(0, l):
        #     if nums
        while val in nums:
            nums.remove(val)
        nums_ = nums
        return len(nums_)


solution = Solution()
print solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
