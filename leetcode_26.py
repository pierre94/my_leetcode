# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_26
@time: 2018/7/8 下午8:00

删除排序数组中的重复项
需要对原来的数据进行变更，所以要用removeDuplicates_by_others
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        return len(nums)


    def removeDuplicates_by_others(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 设置两个指针，low记录非重复项，high依次遍历nums列表
        low = 0
        l = len(nums)
        # 假如nums为空或者只有一个数字
        if l <= 1:
            return l
        else:
            # 依次从nums列表读取元素
            for high in range(l):
                # 当low和high对应的值不相等时，low向前进一位，
                # 并且把high当前所对应的值赋给前进一位后的low，以保证nums从0开始按顺序排列
                if nums[low] < nums[high]:
                    low = low + 1
                    nums[low] = nums[high]
            # low的值+1就是新的长度
            # leetcode会自己打出nums长度范围内的值
            return low + 1


solution = Solution()
print solution.removeDuplicates_by_others([1, 1, 2, 1, 1])
print solution.removeDuplicates([1, 1, 2, 1, 1])
