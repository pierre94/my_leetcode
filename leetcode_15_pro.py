# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: test_leetcode_15_pro
@time: 2018/6/11 12:37 AM
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums_new = []
        # for num in nums:
        #     if num not in nums_new:
        #         nums_new.append(num)
        # nums = nums_new
        # print nums
        nums_len = len(nums)
        result_list = []

        for i in range(0, nums_len):
            for j in range(i + 1, nums_len):
                for k in range(j + 1, nums_len):
                    _list = []
                    if (nums[i] + nums[j] + nums[k] == 0):
                        _list = [nums[i], nums[j], nums[k]]
                        _list.sort()
                        if _list not in result_list:
                            result_list.append(_list)
        return result_list


solution = Solution()
# print solution.threeSum([-1, 0, 1, 2, -1, -4])
print solution.threeSum([13,5,-4,-9,1,-3,10,-7,7,3,1,-13,-11,7,-10,12,-15,13,5,-8,-11,-12,-15,-13,-3,-13,5,-4,6,1,-10,4,13,-7,3,-9,-3,-2,-1,12,9,-15,14,5,0,-10,-5,-8,-12,-15,-1,-8,11,-9,-14,-7,-6,7,-4,-15,-15,-7,-4,14,1,6,12,14,12,-11,11,-2,11,2,-12,-4,7,-2,-5,10,-9,10,9,-13,-14,11,-13,-13,3,-1,9,3,7,-9,-6,-14,4,-8,7,1,-12,-5,14,14,12,10,-12,-3,-7,-2,-8,-9,-7,9,-7,-13,5,-12,-11,-7,2,14,3,-14])
# print solution.threeSum([-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1])
