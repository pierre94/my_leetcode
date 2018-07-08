# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_9
@time: 2018/7/1 下午1:20

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
进阶：不使用字符串 （待研究）
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            str_x = str(x)
            print str_x
            for i in range(0, int(len(str_x) / 2)):
                if str_x[i] != str_x[len(str_x) - i - 1]:
                    return False
        return True


solution = Solution()
print solution.isPalindrome(342)
