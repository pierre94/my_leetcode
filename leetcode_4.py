# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_4
@time: 2018/6/30 下午9:47

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
示例 1:
nums1 = [1, 3]
nums2 = [2]
中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
中位数是 (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1 = list(set(nums1))
        nums1.sort()
        print nums1
        if (len(nums1) % 2) == 0:
            print len(nums1)

            return (round(nums1[(len(nums1)) / 2 - 1]) + round(nums1[len(nums1) / 2])) / 2
        else:
            return nums1[(len(nums1) - 1) / 2]
            # return round(nums1[(len(nums1) - 1) / 2], 1)



nums1 = [4,5,6,8,9]
nums2 = []

solution = Solution()
print solution.findMedianSortedArrays(nums1, nums2)
