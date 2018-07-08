# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: test_leetcode_15
@time: 2018/6/10 11:22 PM
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
                    if (nums[i] + nums[j] + nums[k] == 0):
                        result_list.append([nums[i], nums[j], nums[k]])
        _result_list_len = len(result_list)
        print result_list
        if _result_list_len == 1:
            return result_list

        result_list_no_duplicate = []
        for item in result_list:
            result_list_no_duplicate.append(item)

        for i in range(0, _result_list_len - 1):
            for j in range(i + 1, _result_list_len):
                i_trans = []
                for i1 in range(0, 3):
                    for i2 in range(0, 3):
                        for i3 in range(0, 3):
                            if (i1 != i2) and (i2 != i3) and (i1 != i3):
                                i_trans.append([result_list[i][i1], result_list[i][i2], result_list[i][i3]])
                if result_list[j] in i_trans:
                    # if result_list[i] in result_list_no_duplicate:
                        result_list_no_duplicate.remove(result_list[i])
                        break

        return result_list_no_duplicate


solution = Solution()
# print solution.threeSum([-1, 0, 1, 2, -1, -4])
# print solution.threeSum([0,0,0,0])
# print solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
# print solution.threeSum([3, 0, 3, 2, -4, 0, -3, 2, 2, 0, -1, -5])
print solution.threeSum([-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1])
